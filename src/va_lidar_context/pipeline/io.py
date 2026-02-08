from __future__ import annotations

import hashlib
import time
from pathlib import Path
from typing import Dict


def allocate_output_dir(
    out_dir: Path,
    job_id: str,
    *,
    fixed_job_id: bool,
) -> tuple[Path, str]:
    """Create a unique output directory for a job and return its path + id."""

    suffix = 0
    while True:
        effective_id = job_id if suffix == 0 else f"{job_id}-{suffix:02d}"
        candidate = out_dir / effective_id
        try:
            candidate.mkdir(parents=True, exist_ok=False)
            return candidate, effective_id
        except FileExistsError:
            if fixed_job_id:
                raise ValueError(
                    f"Output folder already exists for job_id={job_id}: {candidate}"
                )
            suffix += 1


def generate_job_id(
    center: tuple[float, float] | None,
    clip_size: float | None,
    units: str | None,
    *,
    time_ns: int | None = None,
) -> str:
    """Generate a deterministic-ish short job id for a run."""

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


def write_job_info(
    path: Path,
    *,
    tile_name: str,
    job_id: str,
    provider: str,
    lat: float | None,
    lon: float | None,
    clip_size: float | None,
    units: str,
    bbox_wgs84: Dict[str, float] | None,
) -> None:
    """Write a simple README.txt with job metadata."""

    center_source = "input"
    if lat is None or lon is None:
        if bbox_wgs84:
            lon = (bbox_wgs84["xmin"] + bbox_wgs84["xmax"]) / 2.0
            lat = (bbox_wgs84["ymin"] + bbox_wgs84["ymax"]) / 2.0
            center_source = "tile_bbox"
        else:
            center_source = "n/a"

    if lat is not None and lon is not None:
        center_text = f"{lat:.6f}, {lon:.6f}"
    else:
        center_text = "n/a"

    if clip_size is not None:
        size_text = f"{clip_size:g} {units}"
    else:
        size_text = "n/a"

    lines = [
        f"tile_name: {tile_name}",
        f"job_id: {job_id}",
        f"provider: {provider}",
        f"center_latlon: {center_text}",
        f"center_source: {center_source}",
        f"clip_size: {size_text}",
    ]

    if bbox_wgs84:
        lines.append(
            "bbox_wgs84: "
            f"xmin={bbox_wgs84['xmin']:.6f}, "
            f"ymin={bbox_wgs84['ymin']:.6f}, "
            f"xmax={bbox_wgs84['xmax']:.6f}, "
            f"ymax={bbox_wgs84['ymax']:.6f}"
        )

    path.write_text("\n".join(lines) + "\n")


def cleanup_intermediates(tile_dir: Path) -> None:
    """Remove intermediate files that aren't needed post-run."""

    for name in ("tile.json", "tile.laz", "footprints.geojson", "tiles_merged.laz"):
        path = tile_dir / name
        if path.exists():
            path.unlink()
    tiles_dir = tile_dir / "tiles"
    if tiles_dir.exists():
        import shutil

        shutil.rmtree(tiles_dir)
