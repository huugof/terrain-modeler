"""In-process job store: Job dataclass, JOBS dict, runner, and persistence helpers."""

from __future__ import annotations

import json
import logging
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from .. import auth_store
from ..config import BuildConfig
from ..pipeline.build import build as build_pipeline
from ..util import is_path_within
from . import settings as _settings
from .forms import merge_prefill_defaults


@dataclass
class Job:
    job_id: str
    status: str
    created_at: float
    user_id: Optional[int] = None
    started_at: Optional[float] = None
    finished_at: Optional[float] = None
    exit_code: Optional[int] = None
    error: Optional[str] = None
    logs: List[str] = field(default_factory=list)
    summary: Dict[str, Any] = field(default_factory=dict)
    change_cond: threading.Condition = field(default_factory=threading.Condition, repr=False)
    change_version: int = 0


JOBS: Dict[str, Job] = {}
JOBS_LOCK = threading.Lock()
_recent_jobs_change_cond = threading.Condition()
_recent_jobs_change_version = 0


class JobLogHandler(logging.Handler):
    def __init__(self, job: Job) -> None:
        super().__init__()
        self.job = job
        self.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        with self.job.change_cond:
            self.job.logs.append(msg)
            _notify_job_change_locked(self.job)


# ---------------------------------------------------------------------------
# Notification helpers
# ---------------------------------------------------------------------------


def _notify_job_change_locked(job: Job) -> None:
    job.change_version += 1
    job.change_cond.notify_all()


def _notify_recent_jobs_change() -> None:
    global _recent_jobs_change_version
    with _recent_jobs_change_cond:
        _recent_jobs_change_version += 1
        _recent_jobs_change_cond.notify_all()


# ---------------------------------------------------------------------------
# Output-directory resolution helpers
# ---------------------------------------------------------------------------

OUTPUT_ARTIFACT_CANDIDATES = (
    "terrain.obj",
    "terrain.mtl",
    "buildings.obj",
    "combined.obj",
    "combined.mtl",
    "terrain.png",
    "contours.dxf",
    "terrain.xyz",
)
PREVIEW_ARTIFACT_CANDIDATES = ("terrain.obj", "buildings.obj", "combined.obj")


def _dir_has_known_outputs(path: Path) -> bool:
    return any((path / name).is_file() for name in OUTPUT_ARTIFACT_CANDIDATES)


def _has_preview_artifacts(artifacts: List[Dict[str, Any]]) -> bool:
    names = {
        str(item.get("name"))
        for item in artifacts
        if isinstance(item, dict) and str(item.get("name") or "").strip()
    }
    return any(name in names for name in PREVIEW_ARTIFACT_CANDIDATES)


def _discover_output_dir_for_job(job_id: str) -> Optional[Path]:
    job_root = _settings.OUT_DIR / job_id
    if not (job_root.exists() and job_root.is_dir()):
        return None
    if not is_path_within(_settings.OUT_DIR, job_root):
        return None
    if _dir_has_known_outputs(job_root):
        return job_root

    reports: List[Path] = []
    for report_path in job_root.rglob("report.json"):
        if "_cache" in report_path.parts:
            continue
        if report_path.is_file():
            reports.append(report_path)
    reports.sort(key=lambda p: p.stat().st_mtime if p.exists() else 0.0, reverse=True)

    for report_path in reports:
        try:
            report = json.loads(report_path.read_text())
        except Exception:
            report = {}
        if isinstance(report, dict):
            output_dir = report.get("output_dir")
            if isinstance(output_dir, str) and output_dir.strip():
                candidate = Path(output_dir).expanduser()
                if (
                    candidate.exists()
                    and candidate.is_dir()
                    and is_path_within(_settings.OUT_DIR, candidate)
                ):
                    return candidate
        parent_dir = report_path.parent
        if parent_dir.is_dir() and _dir_has_known_outputs(parent_dir):
            return parent_dir

    for child in sorted(job_root.iterdir(), key=lambda p: p.name.lower()):
        if child.is_dir() and _dir_has_known_outputs(child):
            return child

    return None


def _collect_outputs(tile_dir: Path) -> Dict[str, Any]:
    if not tile_dir.exists():
        return {"dir": str(tile_dir), "files": []}
    files = [name for name in OUTPUT_ARTIFACT_CANDIDATES if (tile_dir / name).exists()]
    return {"dir": str(tile_dir), "files": files}


def _resolve_job_output_dir(job: Job) -> Optional[Path]:
    outputs = job.summary.get("outputs")
    if isinstance(outputs, dict):
        raw_dir = outputs.get("dir")
        if isinstance(raw_dir, str) and raw_dir.strip():
            candidate = Path(raw_dir).expanduser()
            if (
                candidate.exists()
                and candidate.is_dir()
                and is_path_within(_settings.OUT_DIR, candidate)
            ):
                return candidate

    report_path = job.summary.get("report_path")
    if isinstance(report_path, str) and report_path:
        report_file = Path(report_path).expanduser()
        if report_file.exists() and report_file.is_file():
            candidate = report_file.parent
            if is_path_within(_settings.OUT_DIR, candidate):
                return candidate

    discovered = _discover_output_dir_for_job(job.job_id)
    if discovered is not None:
        return discovered
    default_dir = _settings.OUT_DIR / job.job_id
    if (
        default_dir.exists()
        and default_dir.is_dir()
        and is_path_within(_settings.OUT_DIR, default_dir)
    ):
        return default_dir
    return None


def _list_job_artifacts(job: Job) -> List[Dict[str, Any]]:
    output_dir = _resolve_job_output_dir(job)
    if output_dir is None:
        return []

    artifacts: List[Dict[str, Any]] = []
    seen: set[str] = set()
    outputs = job.summary.get("outputs")
    summary_files: List[str] = []
    if isinstance(outputs, dict) and isinstance(outputs.get("files"), list):
        for value in outputs.get("files"):
            if isinstance(value, str):
                summary_files.append(value.strip())

    for name in summary_files:
        if not name or "/" in name or "\\" in name or name in seen:
            continue
        path = output_dir / name
        if not path.is_file():
            continue
        stat = path.stat()
        artifacts.append({"name": name, "size": int(stat.st_size), "mtime": float(stat.st_mtime)})
        seen.add(name)

    for name in ("terrain.mtl", "combined.mtl"):
        if name in seen:
            continue
        path = output_dir / name
        if not path.is_file():
            continue
        stat = path.stat()
        artifacts.append({"name": name, "size": int(stat.st_size), "mtime": float(stat.st_mtime)})
        seen.add(name)

    if not artifacts:
        for path in sorted(output_dir.iterdir(), key=lambda p: p.name.lower()):
            if not path.is_file():
                continue
            name = path.name
            if name in seen:
                continue
            stat = path.stat()
            artifacts.append(
                {"name": name, "size": int(stat.st_size), "mtime": float(stat.st_mtime)}
            )
            seen.add(name)

    return artifacts


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------


def _rehydrate_jobs_from_store() -> None:
    if _settings.JOB_REHYDRATE_LIMIT <= 0:
        return
    try:
        persisted = auth_store.list_recent_jobs(
            _settings.DB_PATH, limit=_settings.JOB_REHYDRATE_LIMIT
        )
    except Exception:
        return

    restored: List[Job] = []
    for item in persisted:
        job_id = str(item.get("job_id"))
        summary_raw = item.get("summary")
        summary = summary_raw if isinstance(summary_raw, dict) else {}

        artifacts_raw = item.get("artifacts")
        if isinstance(artifacts_raw, list) and artifacts_raw:
            outputs = summary.get("outputs")
            if not isinstance(outputs, dict):
                outputs = {}
            output_files = outputs.get("files")
            if not isinstance(output_files, list) or not output_files:
                outputs["files"] = [
                    str(entry.get("name"))
                    for entry in artifacts_raw
                    if isinstance(entry, dict) and str(entry.get("name") or "").strip()
                ]
            raw_dir = outputs.get("dir")
            if not isinstance(raw_dir, str) or not raw_dir.strip():
                outputs["dir"] = str(_settings.OUT_DIR / job_id)
            summary["outputs"] = outputs
        elif not isinstance(summary.get("outputs"), dict):
            discovered = _discover_output_dir_for_job(job_id)
            if discovered is not None:
                summary["outputs"] = _collect_outputs(discovered)

        created_at = item.get("created_at")
        if not isinstance(created_at, (int, float)):
            created_at = time.time()
        status = str(item.get("status") or "queued")
        error = sanitize_job_error(item.get("error"))
        # Jobs that were in-flight when the server last stopped will never
        # complete — their worker threads are gone.  Reset them to "error" so
        # they don't appear stuck as "running" in the UI forever.
        if status in ("queued", "running"):
            status = "error"
            error = error or "Job interrupted (server restarted)."
        raw_user_id = item.get("user_id")
        user_id = int(raw_user_id) if isinstance(raw_user_id, int) else None

        restored.append(
            Job(
                job_id=job_id,
                status=status,
                created_at=float(created_at),
                user_id=user_id,
                started_at=(
                    float(item["started_at"])
                    if isinstance(item.get("started_at"), (int, float))
                    else None
                ),
                finished_at=(
                    float(item["finished_at"])
                    if isinstance(item.get("finished_at"), (int, float))
                    else None
                ),
                exit_code=(
                    int(item["exit_code"]) if isinstance(item.get("exit_code"), int) else None
                ),
                error=error,
                summary=summary,
            )
        )

    restored.sort(key=lambda job: (job.created_at, job.job_id))
    with JOBS_LOCK:
        for job in restored:
            if job.job_id not in JOBS:
                JOBS[job.job_id] = job


def _persist_job_snapshot(job: Job) -> None:
    if not _settings.AUTH_ENABLED and not _settings.HMAC_KEYS and not _settings.JOB_HISTORY_ENABLED:
        return
    try:
        from .auth import ensure_auth_store  # avoid circular at module level

        ensure_auth_store()
        summary = job.summary if isinstance(job.summary, dict) else {}
        auth_store.upsert_job_snapshot(
            _settings.DB_PATH,
            job.job_id,
            user_id=job.user_id,
            created_at=job.created_at,
            status=job.status,
            started_at=job.started_at,
            finished_at=job.finished_at,
            exit_code=job.exit_code,
            error=job.error,
            summary=summary,
        )
        auth_store.replace_job_artifacts(_settings.DB_PATH, job.job_id, _list_job_artifacts(job))
    except Exception as exc:
        logging.getLogger(__name__).warning(
            "Failed to persist job snapshot for %s: %s",
            job.job_id,
            exc,
        )
        return


# ---------------------------------------------------------------------------
# Queries
# ---------------------------------------------------------------------------


def _jobs_for_user(user: Optional[Dict[str, Any]]) -> List[Job]:
    with JOBS_LOCK:
        jobs = list(JOBS.values())
    if _settings.AUTH_ENABLED:
        if user is None:
            return []
        jobs = [job for job in jobs if job.user_id == user["id"]]
    jobs.sort(key=lambda job: (job.created_at, job.job_id))
    return jobs


def _recent_job_display_name(job: Job, sequence_number: int) -> str:
    custom_name = str(job.summary.get("custom_name") or "").strip()
    if custom_name:
        return custom_name
    legacy_name = str(job.summary.get("name") or "").strip()
    if legacy_name and legacy_name != job.job_id:
        return legacy_name
    return f"Job {max(sequence_number, 1)}"


def _recent_job_payload(job: Job, sequence_number: int) -> Dict[str, Any]:
    from flask import url_for  # imported here to avoid requiring app context at import

    def _safe_form_defaults(value: Any) -> Dict[str, Any]:
        if not isinstance(value, dict):
            return {}
        return merge_prefill_defaults({}, value)

    name = _recent_job_display_name(job, sequence_number)
    is_done = job.status == "done"
    payload: Dict[str, Any] = {
        "job_id": job.job_id,
        "name": name,
        "status": job.status,
        "display_title": name if is_done else "Job running...",
        "form_defaults": _safe_form_defaults(job.summary.get("form_defaults")),
    }
    if job.status not in ("queued", "running"):
        payload["delete_url"] = url_for("bp.job_delete", job_id=job.job_id)
    if not is_done:
        return payload

    artifacts = _list_job_artifacts(job)
    if artifacts:
        payload["download_all_url"] = url_for("bp.job_download_all", job_id=job.job_id)
    if _has_preview_artifacts(artifacts):
        payload["preview_url"] = url_for("bp.job_status", job_id=job.job_id, tab="preview")
    payload["match_settings_url"] = url_for("bp.index", from_job=job.job_id)
    return payload


# ---------------------------------------------------------------------------
# Job runner
# ---------------------------------------------------------------------------


_GENERIC_BUILD_ERROR = "Build failed. Check server logs for details."


def sanitize_job_error(value: Any) -> Optional[str]:
    text = str(value or "").strip()
    if not text:
        return None
    if text == _GENERIC_BUILD_ERROR:
        return text
    if text.startswith("Job interrupted (server restarted)."):
        return text
    return _GENERIC_BUILD_ERROR


def _sanitize_summary_for_response(summary: Dict[str, Any]) -> Dict[str, Any]:
    """Return a copy of summary with server filesystem paths removed."""
    result = dict(summary)
    result.pop("out", None)
    result.pop("report_path", None)
    outputs = result.get("outputs")
    if isinstance(outputs, dict) and "dir" in outputs:
        result["outputs"] = {k: v for k, v in outputs.items() if k != "dir"}
    return result


def _job_logs_payload(job: Job, offset: int) -> Dict[str, Any]:
    safe_offset = max(0, min(offset, len(job.logs)))
    logs = job.logs[safe_offset:]
    next_offset = safe_offset + len(logs)
    raw_summary = job.summary if isinstance(job.summary, dict) else {}
    return {
        "status": job.status,
        "logs": logs,
        "offset": next_offset,
        "error": job.error,
        "exit_code": job.exit_code,
        "summary": _sanitize_summary_for_response(raw_summary),
    }


def _run_build_job(job: Job, cfg: BuildConfig) -> None:
    with job.change_cond:
        job.status = "running"
        job.started_at = time.time()
        _notify_job_change_locked(job)
    _notify_recent_jobs_change()
    if _settings.AUTH_ENABLED:
        auth_store.set_job_status(_settings.DB_PATH, job.job_id, "running")
        if job.user_id is not None:
            auth_store.set_active_job(_settings.DB_PATH, job.job_id, job.user_id, status="running")
    _persist_job_snapshot(job)
    job_logger = logging.getLogger(f"va_lidar_context.job.{job.job_id}")
    job_logger.setLevel(logging.DEBUG)
    job_logger.propagate = False
    handler = JobLogHandler(job)
    job_logger.addHandler(handler)
    result = None
    try:
        result = build_pipeline(cfg)
        with job.change_cond:
            job.exit_code = result.exit_code
            if job.exit_code == 0:
                job.status = "done"
            else:
                job.status = "error"
                job.error = job.error or _GENERIC_BUILD_ERROR
    except Exception as exc:  # pragma: no cover - surface to UI
        with job.change_cond:
            job.status = "error"
            job.error = sanitize_job_error(exc)
        logging.getLogger(__name__).exception("Build %s failed", job.job_id)
        job_logger.exception("Build failed")
    finally:
        with job.change_cond:
            job.finished_at = time.time()
        job_logger.removeHandler(handler)
        if _settings.AUTH_ENABLED:
            auth_store.set_job_status(_settings.DB_PATH, job.job_id, job.status)
            if job.user_id is not None:
                auth_store.finish_active_job(_settings.DB_PATH, job.job_id, job.status)

        output_dir = result.output_dir if result is not None else None
        report_path = (output_dir / "report.json") if output_dir is not None else None
        if report_path is not None and report_path.is_file():
            try:
                report = json.loads(report_path.read_text())
                with job.change_cond:
                    job.summary["report_path"] = str(report_path)
                    job.summary["tile"] = report.get("tile")
                    if report.get("output_dir"):
                        job.summary["out"] = report.get("output_dir")
                    job.summary["job_id"] = report.get("job_id")
                    job.summary["warnings"] = report.get("warnings")
                    job.summary["source_type"] = report.get("source_type")
                    job.summary["outputs"] = _collect_outputs(report_path.parent)
            except Exception:
                pass
        with job.change_cond:
            _notify_job_change_locked(job)
        _notify_recent_jobs_change()
        _persist_job_snapshot(job)
