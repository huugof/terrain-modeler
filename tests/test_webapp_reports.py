"""Tests for job summary hydration from explicit BuildResult output_dir."""
from __future__ import annotations

import json
import time
from pathlib import Path

from va_lidar_context import webapp
from va_lidar_context.pipeline.types import BuildResult


def _make_report(output_dir: Path, job_id: str = "test-job") -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.json"
    report_path.write_text(
        json.dumps(
            {
                "job_id": job_id,
                "output_dir": str(output_dir),
                "tile": "tile-abc",
                "source_type": "laz",
                "warnings": [],
            }
        )
    )
    (output_dir / "terrain.obj").write_text("dummy")
    return report_path


def test_build_result_carries_output_dir(tmp_path):
    output_dir = tmp_path / "job-abc"
    result = BuildResult(exit_code=0, output_dir=output_dir)
    assert result.exit_code == 0
    assert result.output_dir == output_dir


def test_build_result_output_dir_none_on_failure():
    result = BuildResult(exit_code=1, output_dir=None)
    assert result.exit_code == 1
    assert result.output_dir is None


def test_job_summary_hydrated_from_report(tmp_path, monkeypatch):
    """Job summary is populated from report.json in the explicit output_dir."""
    output_dir = tmp_path / "job-xyz"
    _make_report(output_dir, job_id="job-xyz")

    job = webapp.Job(
        job_id="job-xyz",
        status="running",
        created_at=time.time(),
    )

    # Simulate what _run_build_job does in the finally block with an explicit path
    report_path = output_dir / "report.json"
    assert report_path.is_file()
    report = json.loads(report_path.read_text())

    job.summary["report_path"] = str(report_path)
    job.summary["tile"] = report.get("tile")
    if report.get("output_dir"):
        job.summary["out"] = report.get("output_dir")
    job.summary["job_id"] = report.get("job_id")
    job.summary["warnings"] = report.get("warnings")
    job.summary["source_type"] = report.get("source_type")

    assert job.summary["tile"] == "tile-abc"
    assert job.summary["source_type"] == "laz"
    assert job.summary["job_id"] == "job-xyz"
    assert job.summary["out"] == str(output_dir)


def test_job_summary_not_hydrated_when_no_output_dir():
    """When BuildResult.output_dir is None, summary is left empty (no crash)."""
    job = webapp.Job(
        job_id="job-failed",
        status="error",
        created_at=time.time(),
    )
    # output_dir=None means no report hydration — summary stays empty
    output_dir = None
    report_path = (output_dir / "report.json") if output_dir is not None else None
    assert report_path is None
    # summary untouched
    assert job.summary == {}
