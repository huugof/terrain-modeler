from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def write_report(path: Path, report: Dict[str, Any]) -> None:
    """Persist a build report to disk as JSON."""

    path.write_text(json.dumps(report, indent=2, sort_keys=True))
