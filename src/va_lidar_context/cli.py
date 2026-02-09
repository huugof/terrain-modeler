from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from .config import (
    DEFAULT_ALLOW_MULTI_TILE,
    DEFAULT_COMBINE_OUTPUT,
    DEFAULT_EPT_ONLY,
    DEFAULT_FILL_DTM,
    DEFAULT_FILL_HARD,
    DEFAULT_FILL_MAX_DIST,
    DEFAULT_FILL_SMOOTHING,
    DEFAULT_FORMAT,
    DEFAULT_MAX_HEIGHT,
    DEFAULT_MIN_HEIGHT,
    DEFAULT_NAIP_FLIP_U,
    DEFAULT_NAIP_FLIP_V,
    DEFAULT_NAIP_MAX_SIZE,
    DEFAULT_NAIP_PIXEL_SIZE,
    DEFAULT_NAIP_TILED,
    DEFAULT_OUT_DIR,
    DEFAULT_OUTPUTS,
    DEFAULT_PERCENTILE,
    DEFAULT_PREFER_EPT,
    DEFAULT_PROVIDER,
    DEFAULT_RANDOM_SEED,
    DEFAULT_RESOLUTION,
    DEFAULT_ROTATE_Z,
    DEFAULT_TERRAIN_FLIP_Y,
    DEFAULT_TERRAIN_SAMPLE,
    DEFAULT_UNITS,
    BuildConfig,
)
from .pipeline.build import build

OUTPUT_CHOICES = {"buildings", "terrain", "contours", "parcels", "naip", "xyz"}


def parse_outputs(value: str | None) -> tuple[str, ...]:
    if value is None:
        return DEFAULT_OUTPUTS
    cleaned = [v.strip().lower() for v in value.split(",") if v.strip()]
    if not cleaned:
        raise ValueError("--outputs must contain at least one value")
    unknown = [v for v in cleaned if v not in OUTPUT_CHOICES]
    if unknown:
        raise ValueError(
            "Unknown outputs: "
            + ", ".join(sorted(set(unknown)))
            + f" (valid: {', '.join(sorted(OUTPUT_CHOICES))})"
        )
    seen = set()
    result = []
    for v in cleaned:
        if v in seen:
            continue
        result.append(v)
        seen.add(v)
    return tuple(result)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="va-lidar-context")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_cmd = subparsers.add_parser("build", help="Build context mesh for a tile")
    build_cmd.add_argument(
        "tile_name",
        type=str,
        nargs="?",
        default=None,
        help="Tile name (e.g., S13_4899_20). Optional if --center is provided.",
    )
    build_cmd.add_argument(
        "--provider",
        choices=["va", "national"],
        default=DEFAULT_PROVIDER,
        help="Data provider to use (va=VGIN, national=USGS 3DEP).",
    )
    build_cmd.add_argument(
        "--ept-only",
        action="store_true",
        help="National mode only: require EPT coverage and skip LAZ fallback.",
    )
    build_cmd.add_argument(
        "--prefer-ept",
        dest="prefer_ept",
        action="store_true",
        help="Prefer USGS EPT for point clouds (falls back to VGIN/LAZ).",
    )
    build_cmd.add_argument(
        "--no-prefer-ept",
        dest="prefer_ept",
        action="store_false",
        help="Disable EPT preference and use VGIN/LAZ directly.",
    )
    build_cmd.set_defaults(prefer_ept=DEFAULT_PREFER_EPT)
    build_cmd.add_argument("--out", type=Path, default=DEFAULT_OUT_DIR)
    build_cmd.add_argument("--force", action="store_true")
    build_cmd.add_argument(
        "--format", dest="fmt", default=DEFAULT_FORMAT, choices=["obj"]
    )
    build_cmd.add_argument("--units", default=DEFAULT_UNITS, choices=["feet", "meters"])
    build_cmd.add_argument("--resolution", type=float, default=DEFAULT_RESOLUTION)
    build_cmd.add_argument(
        "--percentile", type=int, choices=[90, 95], default=DEFAULT_PERCENTILE
    )
    build_cmd.add_argument("--min-height", type=float, default=DEFAULT_MIN_HEIGHT)
    build_cmd.add_argument("--max-height", type=float, default=DEFAULT_MAX_HEIGHT)
    build_cmd.add_argument("--floor-to-floor", type=float, default=10.0)
    build_cmd.add_argument("--keep-rasters", action="store_true")
    build_cmd.add_argument("--terrain-sample", type=int, default=DEFAULT_TERRAIN_SAMPLE)
    build_cmd.add_argument("--fill-dtm", action="store_true")
    build_cmd.add_argument("--fill-hard", action="store_true")
    build_cmd.add_argument("--fill-max-dist", type=float, default=DEFAULT_FILL_MAX_DIST)
    build_cmd.add_argument("--fill-smoothing", type=int, default=DEFAULT_FILL_SMOOTHING)
    build_cmd.add_argument(
        "--random-heights",
        nargs=2,
        type=float,
        metavar=("MIN", "MAX"),
        help="Override all building heights with a random range in output units.",
    )
    build_cmd.add_argument(
        "--random-seed",
        type=int,
        default=DEFAULT_RANDOM_SEED,
        help="Seed for random heights (optional).",
    )
    build_cmd.add_argument(
        "--naip-pixel-size", type=float, default=DEFAULT_NAIP_PIXEL_SIZE
    )
    build_cmd.add_argument("--naip-max-size", type=int, default=DEFAULT_NAIP_MAX_SIZE)
    build_cmd.add_argument("--naip-tiled", action="store_true")
    build_cmd.add_argument("--naip-flip-u", action="store_true")
    build_cmd.add_argument("--naip-flip-v", action="store_true")
    build_cmd.add_argument(
        "--combine-output",
        action="store_true",
        help="Export a combined OBJ containing terrain + buildings (untextured).",
    )
    build_cmd.add_argument(
        "--contours",
        type=float,
        default=None,
        metavar="INTERVAL",
        help="Generate contour lines at this interval (in output units). Exports to DXF.",
    )
    build_cmd.add_argument(
        "--terrain-flip-y",
        action="store_true",
        help="Mirror only the terrain mesh across the Y axis (keeps buildings unchanged).",
    )
    build_cmd.add_argument(
        "--flip-y",
        action="store_true",
        help="Mirror all meshes across the Y axis (useful if geometry appears flipped north/south).",
    )
    build_cmd.add_argument(
        "--flip-x",
        action="store_true",
        help="Mirror all meshes across the X axis (useful if geometry appears flipped east/west).",
    )
    build_cmd.add_argument(
        "--rotate-z",
        type=float,
        default=DEFAULT_ROTATE_Z,
        help=(
            "Rotate meshes and DXF/XYZ outputs around Z by degrees "
            "(counter-clockwise, around --center)."
        ),
    )
    build_cmd.add_argument(
        "--center",
        nargs=2,
        type=float,
        metavar=("LAT", "LON"),
        help="Center point in lat, lon (WGS84). Requires --size.",
    )
    build_cmd.add_argument(
        "--size",
        type=float,
        default=None,
        help="Clip size (square) in output units. Required with --center.",
    )
    build_cmd.add_argument(
        "--allow-multi-tile",
        action="store_true",
        help="Allow merging adjacent tiles when the clip extends beyond the base tile.",
    )
    build_cmd.add_argument(
        "--outputs",
        type=str,
        default=None,
        help=(
            "Comma-separated outputs. Options: buildings, terrain, contours, parcels, naip, xyz. "
            "Defaults to buildings,terrain."
        ),
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "build":
        try:
            outputs = parse_outputs(args.outputs)
        except ValueError as exc:
            parser.error(str(exc))
        cfg = BuildConfig(
            tile_name=args.tile_name,
            center=tuple(args.center) if args.center else None,
            size=args.size,
            out_dir=args.out,
            force=args.force,
            fmt=args.fmt,
            units=args.units,
            resolution=args.resolution,
            percentile=args.percentile,
            min_height=args.min_height,
            max_height=args.max_height,
            floor_to_floor=args.floor_to_floor,
            keep_rasters=args.keep_rasters,
            terrain_sample=args.terrain_sample,
            fill_dtm=args.fill_dtm,
            fill_hard=args.fill_hard,
            fill_max_dist=args.fill_max_dist,
            fill_smoothing=args.fill_smoothing,
            random_heights_min=args.random_heights[0] if args.random_heights else None,
            random_heights_max=args.random_heights[1] if args.random_heights else None,
            random_seed=args.random_seed,
            naip_pixel_size=args.naip_pixel_size,
            naip_max_size=args.naip_max_size,
            naip_tiled=args.naip_tiled,
            naip_flip_u=args.naip_flip_u,
            naip_flip_v=args.naip_flip_v,
            combine_output=args.combine_output,
            contour_interval=args.contours,
            allow_multi_tile=args.allow_multi_tile,
            prefer_ept=args.prefer_ept,
            flip_y=args.flip_y,
            flip_x=args.flip_x,
            terrain_flip_y=args.terrain_flip_y,
            rotate_z=args.rotate_z,
            provider=args.provider,
            ept_only=args.ept_only,
            outputs=outputs,
        )
        return build(cfg)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
