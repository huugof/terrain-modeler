from __future__ import annotations

import os
import time
from pathlib import Path

from va_lidar_context.webapp import _find_latest_report


def _write_report(path: Path, mtime: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("{}")
    os.utime(path, (mtime, mtime))


def test_find_latest_report_picks_recent_non_cache(tmp_path):
    started_at = time.time()

    old_report = tmp_path / "old" / "report.json"
    recent_report = tmp_path / "recent" / "report.json"
    cache_report = tmp_path / "_cache" / "report.json"

    _write_report(old_report, started_at - 10)
    _write_report(recent_report, started_at)
    _write_report(cache_report, started_at + 1)

    found = _find_latest_report(tmp_path, started_at)
    assert found == recent_report
