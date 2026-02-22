from __future__ import annotations

import json
import logging
import os
import signal
import subprocess
import sys
import threading
from pathlib import Path
from typing import Any, Dict, Iterable
from urllib.parse import urlparse

_cancel_lock = threading.Lock()
_cancel_events: dict[str, threading.Event] = {}
_active_procs: dict[str, subprocess.Popen] = {}
_cancel_ctx = threading.local()


class BuildCancelledError(RuntimeError):
    """Raised when a running build is cancelled by the user."""


def register_cancel_handle(job_id: str) -> None:
    with _cancel_lock:
        _cancel_events.setdefault(job_id, threading.Event())


def clear_cancel_handle(job_id: str) -> None:
    with _cancel_lock:
        _cancel_events.pop(job_id, None)
        _active_procs.pop(job_id, None)


def bind_cancel_job(job_id: str) -> None:
    _cancel_ctx.job_id = job_id


def unbind_cancel_job() -> None:
    if hasattr(_cancel_ctx, "job_id"):
        delattr(_cancel_ctx, "job_id")


def bound_cancel_job_id() -> str | None:
    return getattr(_cancel_ctx, "job_id", None)


def _terminate_process(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    try:
        if os.name == "posix":
            os.killpg(proc.pid, signal.SIGTERM)
        else:
            proc.terminate()
    except Exception:
        pass
    try:
        proc.wait(timeout=5)
        return
    except Exception:
        pass
    try:
        if os.name == "posix":
            os.killpg(proc.pid, signal.SIGKILL)
        else:
            proc.kill()
    except Exception:
        pass


def request_build_cancel(job_id: str) -> bool:
    with _cancel_lock:
        event = _cancel_events.get(job_id)
        proc = _active_procs.get(job_id)
    if event is None:
        return False
    event.set()
    if proc is not None:
        _terminate_process(proc)
    return True


def is_cancel_requested(job_id: str) -> bool:
    with _cancel_lock:
        event = _cancel_events.get(job_id)
    return bool(event and event.is_set())


def check_cancel_requested() -> None:
    job_id = bound_cancel_job_id()
    if not job_id:
        return
    if is_cancel_requested(job_id):
        raise BuildCancelledError("Build canceled by user.")


def run_subprocess(
    args: list[str],
    *,
    check: bool = False,
    capture_output: bool = False,
    text: bool = False,
    input: bytes | str | None = None,
    **kwargs: Any,
) -> subprocess.CompletedProcess:
    """Run subprocess with cooperative cancellation for bound build jobs."""
    job_id = bound_cancel_job_id()
    if not job_id:
        return subprocess.run(
            args,
            check=check,
            capture_output=capture_output,
            text=text,
            input=input,
            **kwargs,
        )

    if capture_output:
        kwargs.setdefault("stdout", subprocess.PIPE)
        kwargs.setdefault("stderr", subprocess.PIPE)
    if text:
        kwargs["text"] = True
    if input is not None:
        kwargs["stdin"] = subprocess.PIPE
    if os.name == "posix":
        kwargs.setdefault("start_new_session", True)

    proc = subprocess.Popen(args, **kwargs)
    with _cancel_lock:
        _active_procs[job_id] = proc

    send_input = input
    while True:
        try:
            stdout, stderr = proc.communicate(input=send_input, timeout=0.2)
            break
        except subprocess.TimeoutExpired:
            send_input = None
            if is_cancel_requested(job_id):
                _terminate_process(proc)
                try:
                    stdout, stderr = proc.communicate(timeout=2)
                except Exception:
                    stdout, stderr = (None, None)
                raise BuildCancelledError("Build canceled by user.")
            continue
    with _cancel_lock:
        current = _active_procs.get(job_id)
        if current is proc:
            _active_procs.pop(job_id, None)
    result = subprocess.CompletedProcess(args, proc.returncode, stdout, stderr)
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(
            result.returncode,
            args,
            output=result.stdout,
            stderr=result.stderr,
        )
    return result


def get_logger(name: str = "va_lidar_context", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger


def require_https_url(url: str) -> None:
    """Raise ValueError if *url* does not use http or https scheme.

    Call this before passing any externally-sourced URL to a subprocess
    (e.g. PDAL) to prevent SSRF via file://, s3://, or other protocols.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(
            f"Unsafe URL scheme {parsed.scheme!r} — only http/https are allowed: {url!r}"
        )


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True))


def download_file(url: str, dest: Path, force: bool = False, chunk_size: int = 1024 * 1024) -> Path:
    import requests

    if dest.exists() and not force:
        return dest
    ensure_dir(dest.parent)
    with requests.get(url, stream=True, timeout=60) as resp:
        resp.raise_for_status()
        with dest.open("wb") as f:
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
    return dest


def http_get_json(url: str, params: Dict[str, Any], timeout: int = 60) -> Dict[str, Any]:
    import requests

    resp = requests.get(url, params=params, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def iter_offsets(total: int, step: int) -> Iterable[int]:
    offset = 0
    while True:
        yield offset
        offset += step
        if offset >= total:
            break


def is_path_within(base_dir: Path, candidate: Path) -> bool:
    """Return True if *candidate* resolves to a path inside *base_dir*."""
    try:
        candidate.resolve().relative_to(base_dir.resolve())
        return True
    except Exception:
        return False
