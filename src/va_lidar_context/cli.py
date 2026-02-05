from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, List

from pyproj import CRS, Transformer
from shapely.geometry import box
from shapely.ops import transform as shp_transform

from .config import BuildConfig
from .heights import (
    FootprintHeight,
    derive_heights,
    get_laz_crs_wkt,
    get_unit_scale,
    reproject_features,
)
from .mesh import (
    DxfExporter,
    apply_scene_transform,
    combine_meshes,
    export_contours_dxf,
    export_mesh,
    export_obj_with_uv,
    export_parcels_dxf,
    extrude_footprints,
    generate_contours_from_raster,
    terrain_mesh_from_raster,
    tree_mesh_from_canopy,
)
from .naip import download_naip_image
from .pdal_surfaces import (
    clip_raster,
    fill_nodata_raster,
    make_canopy_dsm,
    make_chm,
    make_dsm,
    make_dtm,
    make_ndsm,
    merge_lazs,
)
from .util import download_file, ensure_dir, get_logger, read_json, write_json
from .vgin_footprints import fetch_footprints_geojson
from .vgin_parcels import fetch_parcels_geojson
from .vgin_tile import (
    normalize_coordinates,
    tile_lookup,
    tiles_for_bbox,
    tiles_for_point,
)


def _bbox_contains(
    outer_bbox: Dict[str, float],
    inner_bbox: tuple[float, float, float, float],
) -> bool:
    xmin, ymin, xmax, ymax = inner_bbox
    return (
        outer_bbox["xmin"] <= xmin <= outer_bbox["xmax"]
        and outer_bbox["xmin"] <= xmax <= outer_bbox["xmax"]
        and outer_bbox["ymin"] <= ymin <= outer_bbox["ymax"]
        and outer_bbox["ymin"] <= ymax <= outer_bbox["ymax"]
    )


def build_command(cfg: BuildConfig) -> int:
    logger = get_logger()

    # Resolve tile_name from coordinates if not provided
    tile_name = cfg.tile_name
    lon, lat = None, None
    tile_info = None

    if cfg.center_coords is not None:
        # Auto-detect coordinate order
        lon, lat = normalize_coordinates(cfg.center_coords[0], cfg.center_coords[1])
        logger.info(f"Interpreted coordinates as lon={lon}, lat={lat}")

        if tile_name is None:
            # Look up tile from coordinates
            logger.info("Looking up tile from coordinates...")
            tiles = tiles_for_point(lon, lat)
            if len(tiles) > 1:
                logger.warning(
                    f"Multiple tiles found at this location: {[t['tile_name'] for t in tiles]}. "
                    f"Using first: {tiles[0]['tile_name']}"
                )
            tile_info = tiles[0]
            tile_name = tile_info["tile_name"]
            logger.info(f"Found tile: {tile_name}")

    if tile_name is None:
        raise ValueError("Either tile_name or --center coordinates must be provided")

    tile_dir = cfg.out_dir / tile_name
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
    dtm_clip_path = tile_dir / "dtm_clip.tif"
    report_path = tile_dir / "report.json"
    merged_laz_path = tile_dir / "tiles_merged.laz"

    logger.info("Stage 1/6: tile lookup")
    if tile_json.exists() and not cfg.force:
        tile_info = read_json(tile_json)
    else:
        if tile_info is None:
            tile_info = tile_lookup(tile_name)
        write_json(tile_json, tile_info)

    logger.info("Stage 2/6: download LAZ")
    laz_url = tile_info["laz_url"]
    download_file(laz_url, laz_path, force=cfg.force)

    # Read LAZ CRS early for clipping and units
    laz_wkt = get_laz_crs_wkt(str(laz_path))
    laz_crs = CRS.from_wkt(laz_wkt)
    unit_scale = get_unit_scale(laz_crs, cfg.units)

    clip_poly = None
    clip_bbox_wgs84 = None
    tile_infos = [tile_info]
    laz_paths = [laz_path]
    laz_processing_path = laz_path
    multi_tile_used = False

    # Determine clip center: prefer center_coords (new), fall back to legacy options
    has_center = (
        lon is not None
        or cfg.clip_center_lonlat is not None
        or cfg.clip_center_latlon is not None
        or cfg.clip_center_xy is not None
    )

    if cfg.clip_size is not None and not has_center:
        raise ValueError("Provide a clip center with --center or --center-xy")
    if has_center and cfg.clip_size is None:
        raise ValueError("Provide --size when using a clip center")

    if has_center and cfg.clip_size is not None:
        size_laz = cfg.clip_size / unit_scale
        half = size_laz / 2.0

        # Use already-parsed lon/lat from center_coords, or fall back to legacy options
        if lon is not None and lat is not None:
            # Already parsed from center_coords
            pass
        elif cfg.clip_center_lonlat:
            lon, lat = cfg.clip_center_lonlat
        elif cfg.clip_center_latlon:
            lat, lon = cfg.clip_center_latlon

        if lon is not None and lat is not None:
            bbox = tile_info["bbox_wgs84"]
            if not (
                bbox["xmin"] <= lon <= bbox["xmax"]
                and bbox["ymin"] <= lat <= bbox["ymax"]
            ):
                raise ValueError(
                    f"Clip center ({lon}, {lat}) is outside the tile bbox."
                )
            to_laz = Transformer.from_crs("EPSG:4326", laz_crs, always_xy=True)
            cx, cy = to_laz.transform(lon, lat)
        elif cfg.clip_center_xy:
            cx = cfg.clip_center_xy[0] / unit_scale
            cy = cfg.clip_center_xy[1] / unit_scale
        else:
            raise ValueError("No valid clip center provided")

        clip_poly = box(cx - half, cy - half, cx + half, cy + half)

        to_wgs84 = Transformer.from_crs(laz_crs, "EPSG:4326", always_xy=True)
        clip_poly_wgs84 = shp_transform(to_wgs84.transform, clip_poly)
        minx, miny, maxx, maxy = clip_poly_wgs84.bounds
        clip_bbox_wgs84 = (minx, miny, maxx, maxy)

    if clip_bbox_wgs84 is not None:
        bbox = tile_info["bbox_wgs84"]
        spillover = not _bbox_contains(bbox, clip_bbox_wgs84)
        if spillover and cfg.allow_multi_tile:
            logger.info("Clip extends beyond base tile; fetching intersecting tiles...")
            tile_infos = tiles_for_bbox(clip_bbox_wgs84)
            if not tile_infos:
                raise ValueError("No tiles found for clip bbox")

            tile_infos = sorted(
                tile_infos,
                key=lambda t: (t.get("tile_name") != tile_name, t.get("tile_name", "")),
            )

            tiles_dir = tile_dir / "tiles"
            ensure_dir(tiles_dir)
            laz_paths = []
            for info in tile_infos:
                name = info["tile_name"]
                path = laz_path if name == tile_name else tiles_dir / f"{name}.laz"
                download_file(info["laz_url"], path, force=cfg.force)
                laz_paths.append(path)

            if len(laz_paths) > 1:
                base_crs = laz_crs
                needs_reproj = False
                for path in laz_paths:
                    if path == laz_path:
                        continue
                    other_wkt = get_laz_crs_wkt(str(path))
                    try:
                        if not CRS.from_wkt(other_wkt).equals(base_crs):
                            needs_reproj = True
                            break
                    except Exception:
                        if other_wkt != laz_wkt:
                            needs_reproj = True
                            break
                target_srs = laz_wkt if needs_reproj else None
                if cfg.force or not merged_laz_path.exists():
                    merge_lazs(laz_paths, merged_laz_path, target_srs=target_srs)
                laz_processing_path = merged_laz_path
                multi_tile_used = True
        elif spillover:
            logger.warning(
                "Clip extends beyond tile bounds; use --allow-multi-tile to merge adjacent tiles."
            )

    logger.info("Stage 3/7: fetch footprints")
    if footprints_path.exists() and not cfg.force:
        footprints = json.loads(footprints_path.read_text())
    else:
        bbox = tile_info["bbox_wgs84"]
        bbox_tuple = (
            bbox["xmin"],
            bbox["ymin"],
            bbox["xmax"],
            bbox["ymax"],
        )
        if clip_bbox_wgs84:
            bbox_tuple = clip_bbox_wgs84
        footprints = fetch_footprints_geojson(bbox_tuple)
        footprints_path.write_text(json.dumps(footprints))

    logger.info("Stage 4/7: generate rasters")
    dtm_use_path = dtm_path
    if cfg.force or not dtm_path.exists():
        make_dtm(laz_processing_path, dtm_path, cfg.resolution)
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
            make_dsm(laz_processing_path, dsm_path, cfg.resolution)
        if cfg.force or not ndsm_path.exists():
            make_ndsm(dsm_path, dtm_use_path, ndsm_path)

    terrain_source_path = dtm_use_path
    if clip_poly is not None:
        if cfg.force or not dtm_clip_path.exists():
            clip_raster(dtm_use_path, dtm_clip_path, clip_poly)
        terrain_source_path = dtm_clip_path

    logger.info("Stage 5/7: compute heights")

    min_height_laz = cfg.min_height / unit_scale
    max_height_laz = cfg.max_height / unit_scale
    floor_to_floor_laz = cfg.floor_to_floor / unit_scale

    reprojected = reproject_features(footprints, laz_crs)
    if clip_poly is not None:
        reprojected = [f for f in reprojected if f["geometry"].within(clip_poly)]

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
    mesh = None
    if cfg.export_buildings:
        mesh = extrude_footprints(heights, xy_scale=unit_scale, z_scale=unit_scale)
        if mesh is None:
            logger.warning("No mesh produced (empty footprints or extrusion failures)")

    terrain_mesh = terrain_mesh_from_raster(
        str(terrain_source_path),
        xy_scale=unit_scale,
        z_scale=unit_scale,
        sample=cfg.terrain_sample,
    )
    if terrain_mesh is None:
        logger.warning("No terrain mesh produced (empty or invalid DTM)")

    terrain_uv = None
    if terrain_mesh is not None and cfg.naip_texture:
        import rasterio

        with rasterio.open(terrain_source_path) as ds:
            left, bottom, right, top = ds.bounds
            bbox_laz = [
                (left, bottom),
                (left, top),
                (right, top),
                (right, bottom),
            ]

        to_3857_from_laz = Transformer.from_crs(laz_crs, "EPSG:3857", always_xy=True)
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
        terrain_uv = list(zip(u, v))

    if cfg.terrain_flip_y and terrain_mesh is not None:
        bounds = terrain_mesh.bounds
        center_x = (bounds[0][0] + bounds[1][0]) / 2.0
        center_y = (bounds[0][1] + bounds[1][1]) / 2.0
        apply_scene_transform(
            terrain_mesh,
            center_x,
            center_y,
            flip_y=True,
        )

    center_x = None
    center_y = None
    if cfg.flip_x or cfg.flip_y or cfg.rotate_z:
        if terrain_mesh is not None:
            bounds = terrain_mesh.bounds
            center_x = (bounds[0][0] + bounds[1][0]) / 2.0
            center_y = (bounds[0][1] + bounds[1][1]) / 2.0
        elif mesh is not None:
            bounds = mesh.bounds
            center_x = (bounds[0][0] + bounds[1][0]) / 2.0
            center_y = (bounds[0][1] + bounds[1][1]) / 2.0
        else:
            center_x = 0.0
            center_y = 0.0
        apply_scene_transform(
            terrain_mesh,
            center_x,
            center_y,
            flip_x=cfg.flip_x,
            flip_y=cfg.flip_y,
            rotate_deg=cfg.rotate_z,
        )
        apply_scene_transform(
            mesh,
            center_x,
            center_y,
            flip_x=cfg.flip_x,
            flip_y=cfg.flip_y,
            rotate_deg=cfg.rotate_z,
        )

    if mesh is not None:
        export_mesh(mesh, str(mesh_path))

    if terrain_mesh is not None:
        if cfg.naip_texture and terrain_uv is not None:
            export_obj_with_uv(
                terrain_mesh,
                terrain_uv,
                str(terrain_path),
                str(terrain_mtl_path),
                terrain_tex_path.name,
            )
            if cfg.combine_output:
                from .mesh import export_scene_with_terrain_texture

                export_scene_with_terrain_texture(
                    terrain_mesh,
                    terrain_uv,
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
        chm_clip_path = tile_dir / "canopy_height_clip.tif"
        if cfg.force or not canopy_path.exists():
            make_canopy_dsm(laz_processing_path, canopy_path, cfg.trees_resolution)
        if cfg.force or not chm_path.exists():
            make_chm(canopy_path, dtm_use_path, chm_path)
        chm_use_path = chm_path
        if clip_poly is not None:
            if cfg.force or not chm_clip_path.exists():
                clip_raster(chm_path, chm_clip_path, clip_poly)
            chm_use_path = chm_clip_path

        trees_mesh = tree_mesh_from_canopy(
            str(chm_use_path),
            str(terrain_source_path),
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
            if (cfg.flip_x or cfg.flip_y or cfg.rotate_z) and center_x is not None:
                apply_scene_transform(
                    trees_mesh,
                    center_x,
                    center_y,
                    flip_x=cfg.flip_x,
                    flip_y=cfg.flip_y,
                    rotate_deg=cfg.rotate_z,
                )
            export_mesh(trees_mesh, str(trees_path))

    # Export DXF with contours, parcels, and/or building footprints
    export_dxf = cfg.contour_interval is not None or cfg.parcels
    if export_dxf:
        logger.info("Generating DXF export")
        dxf_path = tile_dir / "site.dxf"
        dxf = DxfExporter()

        # Transform function from WGS84 to LAZ CRS
        to_laz = Transformer.from_crs("EPSG:4326", laz_crs, always_xy=True)

        # Add contours
        if cfg.contour_interval is not None:
            interval_laz = cfg.contour_interval / unit_scale
            contours = generate_contours_from_raster(
                str(terrain_source_path),
                interval=interval_laz,
                xy_scale=unit_scale,
                z_scale=unit_scale,
                sample=1,
            )
            if contours:
                # Use 5x interval for major contours
                major_interval = cfg.contour_interval * 5
                contour_count = dxf.add_contours(
                    contours, major_interval=major_interval
                )
                logger.info(f"  Added {contour_count} contour polylines")

        # Add parcels
        if cfg.parcels:
            bbox = tile_info["bbox_wgs84"]
            parcels_bbox = (bbox["xmin"], bbox["ymin"], bbox["xmax"], bbox["ymax"])
            if clip_bbox_wgs84:
                parcels_bbox = clip_bbox_wgs84

            parcels = fetch_parcels_geojson(parcels_bbox)
            parcel_count = dxf.add_polygons_from_geojson(
                parcels,
                layer_name="PARCELS",
                xy_scale=unit_scale,
                transform_func=to_laz.transform,
                color=3,  # Green
            )
            logger.info(f"  Added {parcel_count} parcel boundaries")

        # Always add building footprints when exporting DXF
        building_count = dxf.add_polygons_from_geojson(
            footprints,
            layer_name="BUILDINGS",
            xy_scale=unit_scale,
            transform_func=to_laz.transform,
            color=5,  # Blue
        )
        logger.info(f"  Added {building_count} building footprints")

        dxf.save(str(dxf_path))
        logger.info(f"Exported DXF to {dxf_path}")

    if not cfg.keep_rasters:
        for path in (
            dtm_path,
            dtm_filled_path,
            dtm_clip_path,
            dsm_path,
            ndsm_path,
            tile_dir / "canopy_dsm.tif",
            tile_dir / "canopy_height.tif",
            tile_dir / "canopy_height_clip.tif",
        ):
            if path.exists():
                path.unlink()

    height_values = [h.height * unit_scale for h in heights]
    report: Dict[str, Any] = {
        "tile": tile_name,
        "tiles": {
            "primary": tile_name,
            "count": len(tile_infos),
            "names": [t["tile_name"] for t in tile_infos],
            "merged_laz": merged_laz_path.name if multi_tile_used else None,
        },
        "multi_tile": {
            "enabled": cfg.allow_multi_tile,
            "used": multi_tile_used,
        },
        "units": cfg.units,
        "unit_scale": unit_scale,
        "footprints_total": len(footprints.get("features", [])),
        "footprints_extruded": len(heights),
        "clip": {
            "enabled": clip_poly is not None,
            "center_lonlat": cfg.clip_center_lonlat,
            "center_xy": cfg.clip_center_xy,
            "size": cfg.clip_size,
        },
        "transform": {
            "flip_x": cfg.flip_x,
            "flip_y": cfg.flip_y,
            "rotate_z": cfg.rotate_z,
        },
        "terrain_transform": {
            "flip_y": cfg.terrain_flip_y,
        },
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
        "contours": {
            "enabled": cfg.contour_interval is not None,
            "interval": cfg.contour_interval,
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
    build.add_argument(
        "tile_name",
        type=str,
        nargs="?",
        default=None,
        help="Tile name (e.g., S13_4899_20). Optional if --center is provided.",
    )
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
    build.add_argument(
        "--contours",
        type=float,
        default=None,
        metavar="INTERVAL",
        help="Generate contour lines at this interval (in output units). Exports to DXF.",
    )
    build.add_argument("--no-buildings", action="store_true", help="Skip exporting buildings mesh.")
    build.add_argument(
        "--parcels",
        action="store_true",
        help="Export parcel/plot boundaries to DXF.",
    )
    build.add_argument(
        "--terrain-flip-y",
        action="store_true",
        help="Mirror only the terrain mesh across the Y axis (keeps buildings unchanged).",
    )
    build.add_argument(
        "--flip-y",
        action="store_true",
        help="Mirror all meshes across the Y axis (useful if geometry appears flipped north/south).",
    )
    build.add_argument(
        "--flip-x",
        action="store_true",
        help="Mirror all meshes across the X axis (useful if geometry appears flipped east/west).",
    )
    build.add_argument(
        "--rotate-z",
        type=float,
        default=0.0,
        help="Rotate all meshes around Z by degrees (counter-clockwise).",
    )
    build.add_argument(
        "--center",
        nargs=2,
        type=float,
        metavar=("COORD1", "COORD2"),
        help="Center point coordinates. Order is auto-detected (lat/lon or lon/lat). "
        "If tile_name is omitted, the correct tile is found automatically. Requires --size.",
    )
    build.add_argument(
        "--center-lonlat",
        nargs=2,
        type=float,
        metavar=("LON", "LAT"),
        help="(Legacy) Center of clip region in lon/lat (WGS84). Requires --size.",
    )
    build.add_argument(
        "--center-latlon",
        nargs=2,
        type=float,
        metavar=("LAT", "LON"),
        help="(Legacy) Center of clip region in lat/lon (WGS84). Requires --size.",
    )
    build.add_argument(
        "--center-xy",
        nargs=2,
        type=float,
        metavar=("X", "Y"),
        help="Center of clip region in output units (feet/meters). Requires --size.",
    )
    build.add_argument(
        "--size",
        type=float,
        default=None,
        help="Clip size (square) in output units. Required with --center.",
    )
    build.add_argument(
        "--allow-multi-tile",
        action="store_true",
        help="Allow merging adjacent tiles when the clip extends beyond the base tile.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "build":
        cfg = BuildConfig(
            tile_name=args.tile_name,
            center_coords=tuple(args.center) if args.center else None,
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
            contour_interval=args.contours,
            parcels=args.parcels,
            clip_center_lonlat=tuple(args.center_lonlat)
            if args.center_lonlat
            else None,
            clip_center_latlon=tuple(args.center_latlon)
            if args.center_latlon
            else None,
            clip_center_xy=tuple(args.center_xy) if args.center_xy else None,
            clip_size=args.size,
            allow_multi_tile=args.allow_multi_tile,
            export_buildings=not args.no_buildings,
            flip_y=args.flip_y,
            flip_x=args.flip_x,
            terrain_flip_y=args.terrain_flip_y,
            rotate_z=args.rotate_z,
        )
        return build_command(cfg)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
