from __future__ import annotations

from pathlib import Path

from va_lidar_context.pipeline import io


def test_generate_job_id_stable_with_time_ns():
    job_id = io.generate_job_id((1.0, 2.0), 100.0, "feet", time_ns=123)
    assert len(job_id) == 16
    assert job_id == io.generate_job_id((1.0, 2.0), 100.0, "feet", time_ns=123)


def test_allocate_output_dir_suffix(tmp_path: Path):
    first, first_id = io.allocate_output_dir(tmp_path, "job", fixed_job_id=False)
    assert first.exists()
    second, second_id = io.allocate_output_dir(tmp_path, "job", fixed_job_id=False)
    assert second.exists()
    assert first_id == "job"
    assert second_id == "job-01"
