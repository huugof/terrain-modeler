#!/usr/bin/env python3
"""Preload default Grand Canyon preview assets for the web UI."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from va_lidar_context.config import BuildConfig
from va_lidar_context.pipeline.build import build

DEFAULT_JOB_ID = "grand-canyon-default"
DEFAULT_CENTER = (36.09841234052352, -112.0952885242688)
DEFAULT_SIZE_FEET = 3000.0
DEFAULT_TERRAIN_COMPLEXITY = 5
PREVIEW_ARTIFACTS = ("terrain.obj", "buildings.obj", "combined.obj")


def _has_preview_artifacts(path: Path) -> bool:
    return any((path / name).is_file() for name in PREVIEW_ARTIFACTS)


def _terrain_sample_for_complexity(complexity: int) -> int:
    """Mirror web-app mapping: 0..10 complexity -> terrain sample 11..1."""
    complexity = max(0, min(10, complexity))
    return max(1, 11 - complexity)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build preloaded Grand Canyon preview data for first web-app load."
    )
    parser.add_argument("--out", type=Path, default=Path("./out"))
    parser.add_argument("--job-id", default=DEFAULT_JOB_ID)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild even when preview artifacts already exist.",
    )
    args = parser.parse_args()

    out_dir = args.out.expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)
    target_dir = out_dir / args.job_id

    if target_dir.exists() and _has_preview_artifacts(target_dir) and not args.force:
        print(f"Default preview already exists at {target_dir}")
        return 0

    if target_dir.exists() and args.force:
        shutil.rmtree(target_dir)

    cfg = BuildConfig(
        job_id=args.job_id,
        center=DEFAULT_CENTER,
        size=DEFAULT_SIZE_FEET,
        units="feet",
        out_dir=out_dir,
        provider="national",
        outputs=("buildings", "terrain", "naip"),
        terrain_sample=_terrain_sample_for_complexity(DEFAULT_TERRAIN_COMPLEXITY),
        fill_dtm=True,
        fill_hard=True,
        cleanup_intermediates=True,
    )
    result = build(cfg)
    output_dir = result.get("output_dir") if isinstance(result, dict) else None
    print(f"Preloaded default preview ready at {output_dir or target_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
