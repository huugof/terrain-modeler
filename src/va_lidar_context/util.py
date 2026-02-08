from __future__ import annotations

import hashlib
import json
import logging
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable


def get_logger(
    name: str = "va_lidar_context", level: int = logging.INFO
) -> logging.Logger:
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


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True))


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text())


def download_file(
    url: str, dest: Path, force: bool = False, chunk_size: int = 1024 * 1024
) -> Path:
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


def http_get_json(
    url: str, params: Dict[str, Any], timeout: int = 60
) -> Dict[str, Any]:
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


def generate_job_id(
    center: tuple[float, float] | None,
    clip_size: float | None,
    units: str | None,
    *,
    time_ns: int | None = None,
) -> str:
    if time_ns is None:
        time_ns = time.time_ns()
    if center is None:
        center_text = "n/a"
    else:
        center_text = f"{center[0]:.6f},{center[1]:.6f}"
    size_text = "n/a" if clip_size is None else f"{clip_size:g}"
    units_text = units or "n/a"
    payload = f"{center_text}|{size_text}|{units_text}|{time_ns}"
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return digest[:16]
