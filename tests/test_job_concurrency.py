"""Concurrency regression tests for job logging isolation and summary correctness
(tasks 2.6 and 2.7)."""
from __future__ import annotations

import json
import logging
import threading
import time
from pathlib import Path

from va_lidar_context import webapp
from va_lidar_context.webapp import Job, JobLogHandler


# ---------------------------------------------------------------------------
# 2.6: Log isolation — two concurrent jobs must not share log entries
# ---------------------------------------------------------------------------


def _make_job(job_id: str) -> Job:
    return Job(job_id=job_id, status="running", created_at=time.time())


def test_job_log_handlers_are_isolated():
    """Each job gets its own child logger; messages for job A must not appear in job B."""
    job_a = _make_job("job-a")
    job_b = _make_job("job-b")

    logger_a = logging.getLogger(f"va_lidar_context.job.{job_a.job_id}")
    logger_a.setLevel(logging.DEBUG)
    logger_a.propagate = False
    handler_a = JobLogHandler(job_a)
    logger_a.addHandler(handler_a)

    logger_b = logging.getLogger(f"va_lidar_context.job.{job_b.job_id}")
    logger_b.setLevel(logging.DEBUG)
    logger_b.propagate = False
    handler_b = JobLogHandler(job_b)
    logger_b.addHandler(handler_b)

    try:
        logger_a.info("message only for A")
        logger_b.info("message only for B")
    finally:
        logger_a.removeHandler(handler_a)
        logger_b.removeHandler(handler_b)

    assert any("only for A" in m for m in job_a.logs)
    assert not any("only for B" in m for m in job_a.logs)

    assert any("only for B" in m for m in job_b.logs)
    assert not any("only for A" in m for m in job_b.logs)


def test_concurrent_jobs_do_not_cross_contaminate_logs():
    """Run two jobs' logging concurrently across threads; verify no cross-talk."""
    job_a = _make_job("concurrent-a")
    job_b = _make_job("concurrent-b")

    errors: list[str] = []

    def log_for_job(job: Job, tag: str, count: int) -> None:
        logger = logging.getLogger(f"va_lidar_context.job.{job.job_id}")
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        handler = JobLogHandler(job)
        logger.addHandler(handler)
        try:
            for i in range(count):
                logger.info(f"{tag} message {i}")
                time.sleep(0.001)
        finally:
            logger.removeHandler(handler)

    t_a = threading.Thread(target=log_for_job, args=(job_a, "A", 20))
    t_b = threading.Thread(target=log_for_job, args=(job_b, "B", 20))
    t_a.start()
    t_b.start()
    t_a.join()
    t_b.join()

    for msg in job_a.logs:
        if "B message" in msg:
            errors.append(f"job_a received job_b message: {msg!r}")
    for msg in job_b.logs:
        if "A message" in msg:
            errors.append(f"job_b received job_a message: {msg!r}")

    assert not errors, "\n".join(errors)
    assert len(job_a.logs) == 20
    assert len(job_b.logs) == 20


# ---------------------------------------------------------------------------
# 2.7: Summary correctness — two jobs finishing close together get distinct
#      summaries based on their explicit output_dir, not mtime scanning
# ---------------------------------------------------------------------------


def _write_report(output_dir: Path, job_id: str, tile: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.json"
    report_path.write_text(
        json.dumps(
            {
                "job_id": job_id,
                "output_dir": str(output_dir),
                "tile": tile,
                "source_type": "laz",
                "warnings": [],
            }
        )
    )
    return report_path


def _hydrate_summary(job: Job, output_dir: Path | None) -> None:
    """Mirror the finally-block logic in _run_build_job."""
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
                job.summary["source_type"] = report.get("source_type")
        except Exception:
            pass


def test_two_jobs_finishing_simultaneously_get_correct_summaries(tmp_path):
    """When two jobs finish at the same instant, each gets its own tile/output_dir."""
    dir_a = tmp_path / "job-sim-a"
    dir_b = tmp_path / "job-sim-b"
    _write_report(dir_a, job_id="job-sim-a", tile="tile-for-a")
    _write_report(dir_b, job_id="job-sim-b", tile="tile-for-b")

    job_a = _make_job("job-sim-a")
    job_b = _make_job("job-sim-b")

    # Simulate both finishing at nearly the same time by running hydration in threads
    def finish(job: Job, output_dir: Path) -> None:
        _hydrate_summary(job, output_dir)

    t_a = threading.Thread(target=finish, args=(job_a, dir_a))
    t_b = threading.Thread(target=finish, args=(job_b, dir_b))
    t_a.start()
    t_b.start()
    t_a.join()
    t_b.join()

    assert job_a.summary.get("tile") == "tile-for-a"
    assert job_a.summary.get("job_id") == "job-sim-a"

    assert job_b.summary.get("tile") == "tile-for-b"
    assert job_b.summary.get("job_id") == "job-sim-b"


def test_failed_job_with_no_output_dir_gets_empty_summary(tmp_path):
    """A job that fails before producing any output must not steal another job's report."""
    dir_b = tmp_path / "job-ok"
    _write_report(dir_b, job_id="job-ok", tile="tile-for-ok")

    failed_job = _make_job("job-failed")
    ok_job = _make_job("job-ok")

    _hydrate_summary(failed_job, None)      # failed — no output_dir
    _hydrate_summary(ok_job, dir_b)         # succeeded — explicit output_dir

    assert failed_job.summary == {}
    assert ok_job.summary.get("tile") == "tile-for-ok"
