from __future__ import annotations

import json
import subprocess
from pathlib import Path

import laspy


def run_pdal_pipeline(pipeline: dict) -> None:
    proc = subprocess.run(
        ["pdal", "pipeline", "--stdin"],
        input=json.dumps(pipeline).encode("utf-8"),
        check=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8"))


def _format_bounds(bounds: tuple[float, float, float, float]) -> str:
    minx, miny, maxx, maxy = bounds
    return f"([{minx},{maxx}],[{miny},{maxy}])"


def ept_to_laz(
    ept_url: str,
    laz_path: Path,
    bounds: tuple[float, float, float, float],
) -> Path:
    pipeline = {
        "pipeline": [
            {
                "type": "readers.ept",
                "filename": ept_url,
                "bounds": _format_bounds(bounds),
            },
            {
                "type": "writers.las",
                "filename": str(laz_path),
            },
        ]
    }
    run_pdal_pipeline(pipeline)
    count = laz_point_count(laz_path)
    if count <= 0:
        raise ValueError(
            f"EPT query returned zero points for bounds {_format_bounds(bounds)}"
        )
    return laz_path


def laz_point_count(laz_path: Path) -> int:
    with laspy.open(laz_path) as reader:
        return int(reader.header.point_count or 0)
