from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, List

from pyproj import CRS, Transformer

from .config import BuildConfig
from .heights import (
    FootprintHeight,
    derive_heights,
    get_laz_crs_wkt,
    get_unit_scale,
    reproject_features,
)
from .mesh import (
    combine_meshes,
    export_mesh,
    export_obj_with_uv,
    extrude_footprints,
    terrain_mesh_from_raster,
    tree_mesh_from_canopy,
)
from .naip import download_naip_image
from .pdal_surfaces import (
    fill_nodata_raster,
    make_canopy_dsm,
    make_chm,
    make_dsm,
    make_dtm,
    make_ndsm,
)
from .util import download_file, ensure_dir, get_logger, read_json, write_json
from .vgin_footprints import fetch_footprints_geojson
from .vgin_tile import tile_lookup


def build_command(cfg: BuildConfig) -> int:
    logger = get_logger()
    tile_dir = cfg.out_dir / cfg.tile_name
    ensure_dir(tile_dir)

    tile_json = tile_dir / "tile.json"
    laz_path = tile_dir / "tile.laz"
    footprints_path = tile_dir / "footprints.geojson"
    dtm_path = tile_dir / "dtm.tif"
    dtm_filled_path = tile_dir / "dtm_filled.tif"
    dsm_path = tile_dir / "dsm.tif"
    ndsm_path = tile_dir / "ndsm.tif"
    mesh_path = tile_dir / f"buildings.{cfg.fmt}"
    terrain_path = tile_dir / "terrain.obj"
    terrain_mtl_path = tile_dir / "terrain.mtl"
    terrain_tex_path = tile_dir / "terrain.png"
    trees_path = tile_dir / "trees.obj"
    combined_path = tile_dir / "scene.obj"
    combined_mtl_path = tile_dir / "scene.mtl"
    report_path = tile_dir / "report.json"

    logger.info("Stage 1/6: tile lookup")
    if tile_json.exists() and not cfg.force:
        tile_info = read_json(tile_json)
    else:
        tile_info = tile_lookup(cfg.tile_name)
        write_json(tile_json, tile_info)

    logger.info("Stage 2/6: download LAZ")
    laz_url = tile_info["laz_url"]
    download_file(laz_url, laz_path, force=cfg.force)

    logger.info("Stage 3/6: fetch footprints")
    if footprints_path.exists() and not cfg.force:
        footprints = json.loads(footprints_path.read_text())
    else:
        bbox = tile_info["bbox_wgs84"]
        footprints = fetch_footprints_geojson(
            (bbox["xmin"], bbox["ymin"], bbox["xmax"], bbox["ymax"])
        )
        footprints_path.write_text(json.dumps(footprints))

    logger.info("Stage 4/7: generate rasters")
    dtm_use_path = dtm_path
    if cfg.force or not dtm_path.exists():
        make_dtm(laz_path, dtm_path, cfg.resolution)
    if cfg.fill_dtm:
        if cfg.force or not dtm_filled_path.exists():
            fill_nodata_raster(
                dtm_path,
                dtm_filled_path,
                max_distance=cfg.fill_max_dist,
                smoothing_iterations=cfg.fill_smoothing,
                hard_fill=cfg.fill_hard,
            )
        dtm_use_path = dtm_filled_path
    override_heights = (
        cfg.random_heights_min is not None and cfg.random_heights_max is not None
    )
    if not override_heights:
        if cfg.force or not dsm_path.exists():
            make_dsm(laz_path, dsm_path, cfg.resolution)
        if cfg.force or not ndsm_path.exists():
            make_ndsm(dsm_path, dtm_use_path, ndsm_path)

    logger.info("Stage 5/7: compute heights")
    laz_wkt = get_laz_crs_wkt(str(laz_path))
    laz_crs = CRS.from_wkt(laz_wkt)
    unit_scale = get_unit_scale(laz_crs, cfg.units)

    min_height_laz = cfg.min_height / unit_scale
    max_height_laz = cfg.max_height / unit_scale
    floor_to_floor_laz = cfg.floor_to_floor / unit_scale

    reprojected = reproject_features(footprints, laz_crs)

    override_range = None
    rng = None
    if override_heights:
        if cfg.random_heights_min >= cfg.random_heights_max:
            raise ValueError("random-heights min must be < max")
        override_range = (
            cfg.random_heights_min / unit_scale,
            cfg.random_heights_max / unit_scale,
        )
        rng = random.Random(cfg.random_seed)

    heights, warnings = derive_heights(
        None if override_heights else str(ndsm_path),
        str(dtm_use_path),
        reprojected,
        cfg.percentile,
        min_height_laz,
        max_height_laz,
        floor_to_floor_laz,
        override_height_range=override_range,
        rng=rng,
    )

    logger.info("Stage 6/7: mesh export")
    mesh = extrude_footprints(heights, xy_scale=unit_scale, z_scale=unit_scale)
    if mesh is None:
        logger.warning("No mesh produced (empty footprints or extrusion failures)")
    else:
        export_mesh(mesh, str(mesh_path))

    terrain_mesh = terrain_mesh_from_raster(
        str(dtm_use_path),
        xy_scale=unit_scale,
        z_scale=unit_scale,
        sample=cfg.terrain_sample,
    )
    if terrain_mesh is None:
        logger.warning("No terrain mesh produced (empty or invalid DTM)")
    else:
        if cfg.naip_texture:
            import rasterio

            with rasterio.open(dtm_use_path) as ds:
                left, bottom, right, top = ds.bounds
                bbox_laz = [
                    (left, bottom),
                    (left, top),
                    (right, top),
                    (right, bottom),
                ]

            to_3857_from_laz = Transformer.from_crs(
                laz_crs, "EPSG:3857", always_xy=True
            )
            xs, ys = to_3857_from_laz.transform(
                [p[0] for p in bbox_laz], [p[1] for p in bbox_laz]
            )
            xmin, xmax = min(xs), max(xs)
            ymin, ymax = min(ys), max(ys)

            download_naip_image(
                (xmin, ymin, xmax, ymax),
                terrain_tex_path,
                pixel_size=cfg.naip_pixel_size,
                max_size=cfg.naip_max_size,
            )

            verts = terrain_mesh.vertices
            x_laz = verts[:, 0] / unit_scale
            y_laz = verts[:, 1] / unit_scale
            x3857, y3857 = to_3857_from_laz.transform(x_laz, y_laz)
            u = (x3857 - xmin) / (xmax - xmin)
            v = (y3857 - ymin) / (ymax - ymin)
            v = 1.0 - v
            if cfg.naip_flip_u:
                u = 1.0 - u
            if cfg.naip_flip_v:
                v = 1.0 - v
            uv = list(zip(u, v))
            export_obj_with_uv(
                terrain_mesh,
                uv,
                str(terrain_path),
                str(terrain_mtl_path),
                terrain_tex_path.name,
            )
            if cfg.combine_output:
                from .mesh import export_scene_with_terrain_texture

                export_scene_with_terrain_texture(
                    terrain_mesh,
                    uv,
                    mesh,
                    str(combined_path),
                    str(combined_mtl_path),
                    terrain_tex_path.name,
                )
        else:
            export_mesh(terrain_mesh, str(terrain_path))

    if cfg.combine_output:
        if not cfg.naip_texture:
            combined = combine_meshes([terrain_mesh, mesh])
            if combined is None:
                logger.warning(
                    "No combined mesh produced (missing terrain or buildings)"
                )
            else:
                export_mesh(combined, str(combined_path))

    if cfg.trees:
        logger.info("Stage 7/7: tree blobs")
        canopy_path = tile_dir / "canopy_dsm.tif"
        chm_path = tile_dir / "canopy_height.tif"
        if cfg.force or not canopy_path.exists():
            make_canopy_dsm(laz_path, canopy_path, cfg.trees_resolution)
        if cfg.force or not chm_path.exists():
            make_chm(canopy_path, dtm_use_path, chm_path)

        trees_mesh = tree_mesh_from_canopy(
            str(chm_path),
            str(dtm_use_path),
            xy_scale=unit_scale,
            z_scale=unit_scale,
            sample=cfg.trees_sample,
            min_height=cfg.trees_min_height / unit_scale,
            max_height=cfg.trees_max_height / unit_scale
            if cfg.trees_max_height
            else None,
            radius=cfg.trees_radius / unit_scale,
        )
        if trees_mesh is None:
            logger.warning("No tree mesh produced (empty canopy or filters)")
        else:
            export_mesh(trees_mesh, str(trees_path))

    if not cfg.keep_rasters:
        for path in (
            dtm_path,
            dtm_filled_path,
            dsm_path,
            ndsm_path,
            tile_dir / "canopy_dsm.tif",
            tile_dir / "canopy_height.tif",
        ):
            if path.exists():
                path.unlink()

    height_values = [h.height * unit_scale for h in heights]
    report: Dict[str, Any] = {
        "tile": cfg.tile_name,
        "units": cfg.units,
        "unit_scale": unit_scale,
        "footprints_total": len(footprints.get("features", [])),
        "footprints_extruded": len(heights),
        "percentile": cfg.percentile,
        "random_heights": {
            "enabled": override_heights,
            "min": cfg.random_heights_min if override_heights else None,
            "max": cfg.random_heights_max if override_heights else None,
            "seed": cfg.random_seed if override_heights else None,
        },
        "naip_texture": cfg.naip_texture,
        "naip_pixel_size": cfg.naip_pixel_size if cfg.naip_texture else None,
        "naip_max_size": cfg.naip_max_size if cfg.naip_texture else None,
        "trees": {
            "enabled": cfg.trees,
            "resolution": cfg.trees_resolution if cfg.trees else None,
            "sample": cfg.trees_sample if cfg.trees else None,
            "min_height": cfg.trees_min_height if cfg.trees else None,
            "max_height": cfg.trees_max_height if cfg.trees else None,
            "radius": cfg.trees_radius if cfg.trees else None,
        },
        "dtm_filled": cfg.fill_dtm,
        "dtm_fill_hard": cfg.fill_hard if cfg.fill_dtm else None,
        "dtm_fill_max_dist": cfg.fill_max_dist if cfg.fill_dtm else None,
        "dtm_fill_smoothing": cfg.fill_smoothing if cfg.fill_dtm else None,
        "height_stats": {
            "min": min(height_values) if height_values else None,
            "max": max(height_values) if height_values else None,
            "mean": mean(height_values) if height_values else None,
            "median": median(height_values) if height_values else None,
        },
        "warnings": warnings,
    }
    write_json(report_path, report)

    logger.info("Done")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="va-lidar-context")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build context mesh for a tile")
    build.add_argument("tile_name", type=str)
    build.add_argument("--out", type=Path, default=Path("./out"))
    build.add_argument("--force", action="store_true")
    build.add_argument("--format", dest="fmt", default="obj", choices=["obj"])
    build.add_argument("--units", default="feet", choices=["feet", "meters"])
    build.add_argument("--resolution", type=float, default=1.0)
    build.add_argument("--percentile", type=int, choices=[90, 95], default=95)
    build.add_argument("--min-height", type=float, default=8.0)
    build.add_argument("--max-height", type=float, default=300.0)
    build.add_argument("--floor-to-floor", type=float, default=10.0)
    build.add_argument("--keep-rasters", action="store_true")
    build.add_argument("--terrain-sample", type=int, default=1)
    build.add_argument("--fill-dtm", action="store_true")
    build.add_argument("--fill-hard", action="store_true")
    build.add_argument("--fill-max-dist", type=float, default=10.0)
    build.add_argument("--fill-smoothing", type=int, default=0)
    build.add_argument(
        "--random-heights",
        nargs=2,
        type=float,
        metavar=("MIN", "MAX"),
        help="Override all building heights with a random range in output units.",
    )
    build.add_argument(
        "--random-seed",
        type=int,
        default=None,
        help="Seed for random heights (optional).",
    )
    build.add_argument("--naip-texture", action="store_true")
    build.add_argument("--naip-pixel-size", type=float, default=1.0)
    build.add_argument("--naip-max-size", type=int, default=4000)
    build.add_argument("--naip-flip-u", action="store_true")
    build.add_argument("--naip-flip-v", action="store_true")
    build.add_argument(
        "--combine-output",
        action="store_true",
        help="Export a combined OBJ containing terrain + buildings (untextured).",
    )
    build.add_argument("--trees", action="store_true")
    build.add_argument("--trees-resolution", type=float, default=2.0)
    build.add_argument("--trees-sample", type=int, default=2)
    build.add_argument("--trees-min-height", type=float, default=10.0)
    build.add_argument("--trees-max-height", type=float, default=None)
    build.add_argument("--trees-radius", type=float, default=6.0)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "build":
        cfg = BuildConfig(
            tile_name=args.tile_name,
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
            naip_texture=args.naip_texture,
            naip_pixel_size=args.naip_pixel_size,
            naip_max_size=args.naip_max_size,
            naip_flip_u=args.naip_flip_u,
            naip_flip_v=args.naip_flip_v,
            combine_output=args.combine_output,
            trees=args.trees,
            trees_resolution=args.trees_resolution,
            trees_sample=args.trees_sample,
            trees_min_height=args.trees_min_height,
            trees_max_height=args.trees_max_height,
            trees_radius=args.trees_radius,
        )
        return build_command(cfg)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
