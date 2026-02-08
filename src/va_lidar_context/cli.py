from __future__ import annotations

import argparse
import json
import random
import shutil
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, List

from pyproj import CRS, Transformer
from shapely.geometry import box
from shapely.ops import transform as shp_transform

from .config import DEFAULT_OUT_DIR, BuildConfig
from .heights import (
    FEET_PER_METER,
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
from .naip import download_naip_image, download_naip_image_tiled
from .pdal_surfaces import (
    clip_raster,
    ept_to_laz,
    fill_nodata_raster,
    make_canopy_dsm,
    make_chm,
    make_dsm,
    make_dtm,
    make_dtm_unclassified,
    make_ndsm,
    merge_lazs,
    raster_has_data,
)
from .providers.national_footprints import (
    fetch_footprints_geojson as fetch_national_footprints_geojson,
)
from .providers.rockyweb_health import check_rockyweb
from .providers.usgs_ept import resolve_ept_from_bbox, resolve_ept_from_point
from .providers.usgs_laz import build_laz_index, list_laz_urls, select_laz_tiles
from .providers.usgs_lidar_index import query_for_point, select_best_feature
from .util import (
    download_file,
    ensure_dir,
    generate_job_id,
    get_logger,
    write_json,
)
from .vgin_footprints import fetch_footprints_geojson as fetch_vgin_footprints_geojson
from .parcels.registry import fetch_parcels_for_bbox
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


def _national_job_name(lon: float, lat: float, size: float | None, units: str) -> str:
    if size is None:
        return f"national_{lat:.5f}_{lon:.5f}"
    suffix = f"{size:g}{units[0]}"
    return f"national_{lat:.5f}_{lon:.5f}_{suffix}"


def _image_job_name(lon: float, lat: float, size: float, units: str) -> str:
    suffix = f"{size:g}{units[0]}"
    return f"image_{lat:.5f}_{lon:.5f}_{suffix}"


def _allocate_output_dir(
    out_dir: Path,
    job_id: str,
    *,
    fixed_job_id: bool,
) -> tuple[Path, str]:
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


def _write_job_info(
    path: Path,
    *,
    tile_name: str,
    job_id: str,
    provider: str,
    lon: float | None,
    lat: float | None,
    clip_size: float | None,
    units: str,
    bbox_wgs84: dict[str, float] | None,
) -> None:
    center_source = "input"
    if lon is None or lat is None:
        if bbox_wgs84:
            lon = (bbox_wgs84["xmin"] + bbox_wgs84["xmax"]) / 2.0
            lat = (bbox_wgs84["ymin"] + bbox_wgs84["ymax"]) / 2.0
            center_source = "tile_bbox"
        else:
            center_source = "n/a"

    if lon is not None and lat is not None:
        center_text = f"{lon:.6f}, {lat:.6f}"
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
        f"center_lonlat: {center_text}",
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


def _cleanup_intermediates(tile_dir: Path) -> None:
    for name in ("tile.json", "tile.laz", "footprints.geojson", "tiles_merged.laz"):
        path = tile_dir / name
        if path.exists():
            path.unlink()
    tiles_dir = tile_dir / "tiles"
    if tiles_dir.exists():
        shutil.rmtree(tiles_dir)


def _bbox_from_center_wgs84(
    lon: float,
    lat: float,
    size: float,
    units: str,
) -> tuple[float, float, float, float]:
    if units == "feet":
        size_m = size / FEET_PER_METER
    else:
        size_m = size
    half = size_m / 2.0
    to_merc = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
    to_wgs = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)
    cx, cy = to_merc.transform(lon, lat)
    minx, miny = cx - half, cy - half
    maxx, maxy = cx + half, cy + half
    corners = [
        to_wgs.transform(minx, miny),
        to_wgs.transform(minx, maxy),
        to_wgs.transform(maxx, miny),
        to_wgs.transform(maxx, maxy),
    ]
    xs = [c[0] for c in corners]
    ys = [c[1] for c in corners]
    return (min(xs), min(ys), max(xs), max(ys))


def build_command(cfg: BuildConfig) -> int:
    logger = get_logger()
    provider = cfg.provider
    warnings: list[str] = []
    source_type_used: str | None = None
    naip_tiled_used: bool | None = cfg.naip_tiled if cfg.naip_texture else None

    # Resolve center coordinates (WGS84)
    tile_name = cfg.tile_name
    lon, lat = None, None
    tile_info = None

    if cfg.center_coords is not None:
        # Auto-detect coordinate order
        lon, lat = normalize_coordinates(cfg.center_coords[0], cfg.center_coords[1])
        logger.info(f"Interpreted coordinates as lon={lon}, lat={lat}")
    elif cfg.clip_center_lonlat:
        lon, lat = cfg.clip_center_lonlat
    elif cfg.clip_center_latlon:
        lat, lon = cfg.clip_center_latlon

    clip_bbox_wgs84_hint = None
    if lon is not None and lat is not None and cfg.clip_size is not None:
        clip_bbox_wgs84_hint = _bbox_from_center_wgs84(
            lon, lat, cfg.clip_size, cfg.units
        )

    image_only = (
        cfg.naip_texture
        and not cfg.export_terrain
        and not cfg.export_buildings
        and cfg.contour_interval is None
        and not cfg.trees
        and not cfg.parcels
    )

    if image_only:
        if lon is None or lat is None or cfg.clip_size is None:
            raise ValueError(
                "Image-only output requires center coordinates and --size."
            )
        if tile_name is None:
            tile_name = _image_job_name(lon, lat, cfg.clip_size, cfg.units)
        job_id = cfg.job_id or generate_job_id(
            (lon, lat),
            cfg.clip_size,
            cfg.units,
        )
        tile_dir, job_id = _allocate_output_dir(
            cfg.out_dir, job_id, fixed_job_id=cfg.job_id is not None
        )
        _write_job_info(
            tile_dir / "README.txt",
            tile_name=tile_name,
            job_id=job_id,
            provider=provider,
            lon=lon,
            lat=lat,
            clip_size=cfg.clip_size,
            units=cfg.units,
            bbox_wgs84=None,
        )
        terrain_tex_path = tile_dir / "terrain.png"
        report_path = tile_dir / "report.json"

        logger.info("Stage 1/2: download NAIP image")
        size_m = (
            cfg.clip_size / FEET_PER_METER if cfg.units == "feet" else cfg.clip_size
        )
        half = size_m / 2.0
        to_merc = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
        cx, cy = to_merc.transform(lon, lat)
        bbox_3857 = (cx - half, cy - half, cx + half, cy + half)
        try:
            if cfg.naip_tiled:
                download_naip_image_tiled(
                    bbox_3857,
                    terrain_tex_path,
                    pixel_size=cfg.naip_pixel_size,
                    tile_max_size=cfg.naip_max_size,
                )
            else:
                download_naip_image(
                    bbox_3857,
                    terrain_tex_path,
                    pixel_size=cfg.naip_pixel_size,
                    max_size=cfg.naip_max_size,
                )
        except Exception as exc:
            if cfg.naip_tiled:
                raise
            msg = f"Single NAIP download failed; retrying tiled ({exc})"
            logger.warning(msg)
            warnings.append(msg)
            naip_tiled_used = True
            download_naip_image_tiled(
                bbox_3857,
                terrain_tex_path,
                pixel_size=cfg.naip_pixel_size,
                tile_max_size=cfg.naip_max_size,
            )

        report = {
            "job_id": job_id,
            "output_dir": str(tile_dir),
            "tile": tile_name,
            "provider": provider,
            "source_type": "naip",
            "units": cfg.units,
            "clip": {
                "enabled": True,
                "center_lonlat": (lon, lat),
                "size": cfg.clip_size,
            },
            "naip_texture": True,
            "naip_pixel_size": cfg.naip_pixel_size,
            "naip_max_size": cfg.naip_max_size,
            "naip_tiled": naip_tiled_used,
            "warnings": warnings,
        }
        write_json(report_path, report)
        if cfg.cleanup_intermediates:
            _cleanup_intermediates(tile_dir)
        logger.info("Done (image-only)")
        return 0

    if provider == "va":
        if lon is not None and tile_name is None:
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
            raise ValueError(
                "Either tile_name or --center coordinates must be provided"
            )
    else:
        if lon is None or lat is None:
            raise ValueError("National provider requires --center coordinates")
        if tile_name is None:
            tile_name = _national_job_name(lon, lat, cfg.clip_size, cfg.units)

    cache_dir = cfg.out_dir / "_cache"

    def _build_laz_fallback_tile_info() -> Dict[str, Any]:
        features = query_for_point(lon, lat)
        if not features:
            raise ValueError("No USGS LiDAR workunits found at this location")
        feature = select_best_feature(features)
        attrs = feature.get("attributes", {})
        if not attrs.get("lpc_link"):
            raise ValueError("USGS LiDAR index missing LPC link for fallback")
        return {
            "tile_name": tile_name,
            "provider": "national",
            "source_type": "laz",
            "workunit": attrs.get("workunit"),
            "project": attrs.get("project"),
            "ql": attrs.get("ql"),
            "collect_start": attrs.get("collect_start"),
            "collect_end": attrs.get("collect_end"),
            "lpc_link": attrs.get("lpc_link"),
            "metadata_link": attrs.get("metadata_link"),
        }

    logger.info("Stage 1/6: tile lookup")
    if provider == "va":
        tile_info = tile_lookup(tile_name)
    else:
        if cfg.clip_size is None:
            raise ValueError("National provider requires --size")
        ept_source = None
        if clip_bbox_wgs84_hint is not None:
            ept_source = resolve_ept_from_bbox(
                clip_bbox_wgs84_hint, logger=logger, cache_dir=cache_dir
            )
        if ept_source is None:
            ept_source = resolve_ept_from_point(
                lon, lat, logger=logger, cache_dir=cache_dir
            )
        if ept_source:
            tile_info = {
                "tile_name": tile_name,
                "provider": "national",
                "source_type": "ept",
                "ept_url": ept_source.uri,
                "crs_wkt": ept_source.crs_wkt,
                "bbox_wgs84": {
                    "xmin": ept_source.bbox_wgs84[0],
                    "ymin": ept_source.bbox_wgs84[1],
                    "xmax": ept_source.bbox_wgs84[2],
                    "ymax": ept_source.bbox_wgs84[3],
                },
                **ept_source.metadata,
            }
        else:
            if cfg.ept_only:
                raise ValueError(
                    "EPT coverage not available for this location "
                    "(use another location or disable --ept-only)"
                )
            tile_info = _build_laz_fallback_tile_info()

    job_center = (lon, lat)
    if (lon is None or lat is None) and tile_info:
        bbox = tile_info.get("bbox_wgs84")
        if bbox:
            job_center = (
                (bbox["xmin"] + bbox["xmax"]) / 2.0,
                (bbox["ymin"] + bbox["ymax"]) / 2.0,
            )

    job_id = cfg.job_id or generate_job_id(
        job_center
        if (job_center[0] is not None and job_center[1] is not None)
        else None,
        cfg.clip_size,
        cfg.units,
    )
    tile_dir, job_id = _allocate_output_dir(
        cfg.out_dir, job_id, fixed_job_id=cfg.job_id is not None
    )

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
    combined_path = tile_dir / "combined.obj"
    combined_mtl_path = tile_dir / "combined.mtl"
    dtm_clip_path = tile_dir / "dtm_clip.tif"
    report_path = tile_dir / "report.json"
    merged_laz_path = tile_dir / "tiles_merged.laz"

    write_json(tile_json, tile_info)

    _write_job_info(
        tile_dir / "README.txt",
        tile_name=tile_name,
        job_id=job_id,
        provider=provider,
        lon=lon,
        lat=lat,
        clip_size=cfg.clip_size,
        units=cfg.units,
        bbox_wgs84=tile_info.get("bbox_wgs84") if tile_info else None,
    )

    if provider != "va" and tile_info:
        coverage_status = tile_info.get("coverage_status")
        if coverage_status == "partial":
            ratio = tile_info.get("coverage_ratio")
            if ratio is not None:
                msg = (
                    "EPT coverage is partial for the requested clip "
                    f"(~{ratio * 100:.1f}% covered). Output may be incomplete."
                )
            else:
                msg = (
                    "EPT coverage is partial for the requested clip. "
                    "Output may be incomplete."
                )
            logger.warning(msg)
            warnings.append(msg)

    logger.info("Stage 2/6: download LAZ")
    if provider == "va":
        use_ept = (
            cfg.prefer_ept
            and lon is not None
            and lat is not None
            and cfg.clip_size is not None
        )
        if use_ept:
            ept_source = None
            if clip_bbox_wgs84_hint is not None:
                ept_source = resolve_ept_from_bbox(
                    clip_bbox_wgs84_hint, logger=logger, cache_dir=cache_dir
                )
            if ept_source is None:
                ept_source = resolve_ept_from_point(
                    lon, lat, logger=logger, cache_dir=cache_dir
                )
            if ept_source is not None and ept_source.crs_wkt:
                ept_crs = CRS.from_wkt(ept_source.crs_wkt)
                unit_scale = get_unit_scale(ept_crs, cfg.units)
                size_laz = cfg.clip_size / unit_scale
                half = size_laz / 2.0
                to_laz = Transformer.from_crs("EPSG:4326", ept_crs, always_xy=True)
                cx, cy = to_laz.transform(lon, lat)
                bounds = (cx - half, cy - half, cx + half, cy + half)
                try:
                    ept_to_laz(ept_source.uri, laz_path, bounds)
                    tile_infos = [tile_info]
                    laz_paths = [laz_path]
                    laz_processing_path = laz_path
                    multi_tile_used = False
                    source_type_used = "ept"
                except Exception as exc:
                    msg = f"EPT fetch failed; falling back to VGIN LAZ ({exc})"
                    logger.warning(msg)
                    warnings.append(msg)
                    use_ept = False
            else:
                msg = "EPT coverage not available; falling back to VGIN LAZ."
                logger.warning(msg)
                warnings.append(msg)
                use_ept = False
        if not use_ept:
            laz_url = tile_info["laz_url"]
            download_file(laz_url, laz_path, force=cfg.force)
            tile_infos = [tile_info]
            laz_paths = [laz_path]
            laz_processing_path = laz_path
            multi_tile_used = False
            source_type_used = "laz"
    else:
        source_type = tile_info.get("source_type")
        if source_type == "ept":
            ept_url = tile_info.get("ept_url")
            ept_wkt = tile_info.get("crs_wkt")
            if not ept_url:
                raise ValueError("Missing EPT URL in tile info")
            if not ept_wkt:
                ept_source = resolve_ept_from_point(
                    lon, lat, logger=logger, cache_dir=cache_dir
                )
                if ept_source is None or not ept_source.crs_wkt:
                    raise ValueError("Failed to resolve EPT CRS")
                ept_wkt = ept_source.crs_wkt
                tile_info["crs_wkt"] = ept_wkt
                write_json(tile_json, tile_info)
            ept_crs = CRS.from_wkt(ept_wkt)
            unit_scale = get_unit_scale(ept_crs, cfg.units)
            size_laz = cfg.clip_size / unit_scale
            half = size_laz / 2.0
            to_laz = Transformer.from_crs("EPSG:4326", ept_crs, always_xy=True)
            cx, cy = to_laz.transform(lon, lat)
            bounds = (cx - half, cy - half, cx + half, cy + half)
            try:
                if cfg.force or not laz_path.exists():
                    ept_to_laz(ept_url, laz_path, bounds)
                tile_infos = [tile_info]
                laz_paths = [laz_path]
                laz_processing_path = laz_path
                multi_tile_used = False
                source_type_used = "ept"
            except Exception as exc:
                if cfg.ept_only:
                    raise
                msg = f"EPT fetch failed; falling back to LAZ ({exc})"
                logger.warning(msg)
                warnings.append(msg)
                tile_info = _build_laz_fallback_tile_info()
                source_type = "laz"
        if source_type == "laz":
            health = check_rockyweb(cache_dir / "rockyweb_health.json", logger=logger)
            if not health.get("ok"):
                raise ValueError(
                    "rockyweb is unavailable (EPT missing and LAZ fallback blocked). "
                    f"status={health.get('status')} error={health.get('error')}"
                )
            lpc_link = tile_info.get("lpc_link")
            if not lpc_link:
                raise ValueError("Missing LPC link for LAZ fallback")
            laz_urls = list_laz_urls(lpc_link, logger=logger)
            if not laz_urls:
                raise ValueError("No LAZ URLs found for workunit")
            if cfg.clip_size is None:
                raise ValueError("National provider requires --size")
            if clip_bbox_wgs84_hint is None:
                clip_bbox_wgs84_hint = _bbox_from_center_wgs84(
                    lon, lat, cfg.clip_size, cfg.units
                )
            cache_dir = cfg.out_dir / "_cache" / "usgs_laz"
            workunit = tile_info.get("workunit", "workunit")
            cache_path = cache_dir / f"{workunit}.json"
            tiles_index = build_laz_index(
                laz_urls, cache_path, force=cfg.force, logger=logger
            )
            selected = select_laz_tiles(tiles_index, clip_bbox_wgs84_hint)
            if not selected:
                raise ValueError("No LAZ tiles intersect clip bbox")
            tiles_dir = tile_dir / "tiles"
            ensure_dir(tiles_dir)
            laz_paths = []
            for idx, tile in enumerate(selected):
                local = laz_path if idx == 0 else tiles_dir / Path(tile.url).name
                download_file(tile.url, local, force=cfg.force)
                laz_paths.append(local)
            if len(laz_paths) > 1:
                merge_lazs(laz_paths, merged_laz_path)
                laz_processing_path = merged_laz_path
                multi_tile_used = True
            else:
                laz_processing_path = laz_paths[0]
                multi_tile_used = False
            tile_infos = [tile_info]
            source_type_used = "laz"
        elif source_type == "ept":
            # EPT path already resolved successfully above.
            pass
        else:
            raise ValueError(
                f"Unknown source_type for national provider: {source_type}"
            )

    # Read LAZ CRS early for clipping and units
    laz_wkt = get_laz_crs_wkt(str(laz_path))
    laz_crs = CRS.from_wkt(laz_wkt)
    unit_scale = get_unit_scale(laz_crs, cfg.units)

    clip_poly = None
    clip_bbox_wgs84 = None

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
            if provider == "va":
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

    if clip_bbox_wgs84 is not None and provider == "va" and source_type_used != "ept":
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
        if provider == "va":
            bbox = tile_info["bbox_wgs84"]
            bbox_tuple = (
                bbox["xmin"],
                bbox["ymin"],
                bbox["xmax"],
                bbox["ymax"],
            )
            if clip_bbox_wgs84:
                bbox_tuple = clip_bbox_wgs84
            footprints = fetch_vgin_footprints_geojson(bbox_tuple)
        else:
            if clip_bbox_wgs84 is None:
                raise ValueError(
                    "National provider requires a clip bbox for footprints"
                )
            footprints = fetch_national_footprints_geojson(clip_bbox_wgs84)
        footprints_path.write_text(json.dumps(footprints))

    logger.info("Stage 4/7: generate rasters")
    dtm_use_path = dtm_path
    if cfg.force or not dtm_path.exists():
        make_dtm(laz_processing_path, dtm_path, cfg.resolution)
        if not raster_has_data(dtm_path):
            logger.warning(
                "DTM contains no ground data; falling back to unclassified min raster"
            )
            make_dtm_unclassified(laz_processing_path, dtm_path, cfg.resolution)
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
        reprojected = [f for f in reprojected if f["geometry"].intersects(clip_poly)]
    if not reprojected:
        logger.warning("No footprints intersect the clip area after reprojection")

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

    heights, height_warnings = derive_heights(
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
    warnings.extend(height_warnings)

    logger.info("Stage 6/7: mesh export")
    mesh = None
    if cfg.export_buildings:
        mesh = extrude_footprints(heights, xy_scale=unit_scale, z_scale=unit_scale)
        if mesh is None:
            logger.warning("No mesh produced (empty footprints or extrusion failures)")

    terrain_mesh = None
    terrain_uv = None
    if cfg.export_terrain:
        terrain_mesh = terrain_mesh_from_raster(
            str(terrain_source_path),
            xy_scale=unit_scale,
            z_scale=unit_scale,
            sample=cfg.terrain_sample,
        )
        if terrain_mesh is None:
            logger.warning("No terrain mesh produced (empty or invalid DTM)")

    uv_context = None
    if cfg.naip_texture:
        import rasterio

        with rasterio.open(terrain_source_path) as ds:
            left, bottom, right, top = ds.bounds
            transform = ds.transform
            raster_width = ds.width
            raster_height = ds.height
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
        use_raster_uv = False
        try:
            epsg = laz_crs.to_epsg()
        except Exception:
            epsg = None
        if epsg == 3857:
            use_raster_uv = True
        if abs(transform.b) > 1e-9 or abs(transform.d) > 1e-9:
            use_raster_uv = True
        uv_context = (
            xmin,
            xmax,
            ymin,
            ymax,
            to_3857_from_laz,
            transform,
            raster_width,
            raster_height,
            use_raster_uv,
        )

        try:
            if cfg.naip_tiled:
                download_naip_image_tiled(
                    (xmin, ymin, xmax, ymax),
                    terrain_tex_path,
                    pixel_size=cfg.naip_pixel_size,
                    tile_max_size=cfg.naip_max_size,
                )
            else:
                download_naip_image(
                    (xmin, ymin, xmax, ymax),
                    terrain_tex_path,
                    pixel_size=cfg.naip_pixel_size,
                    max_size=cfg.naip_max_size,
                )
        except Exception as exc:
            if cfg.naip_tiled:
                raise
            msg = f"Single NAIP download failed; retrying tiled ({exc})"
            logger.warning(msg)
            warnings.append(msg)
            naip_tiled_used = True
            download_naip_image_tiled(
                (xmin, ymin, xmax, ymax),
                terrain_tex_path,
                pixel_size=cfg.naip_pixel_size,
                tile_max_size=cfg.naip_max_size,
            )

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

    if cfg.naip_texture and terrain_mesh is not None and uv_context is not None:
        (
            xmin,
            xmax,
            ymin,
            ymax,
            to_3857_from_laz,
            transform,
            raster_width,
            raster_height,
            use_raster_uv,
        ) = uv_context
        verts = terrain_mesh.vertices
        x_laz = verts[:, 0] / unit_scale
        y_laz = verts[:, 1] / unit_scale
        if use_raster_uv:
            inv = ~transform
            col = inv.a * x_laz + inv.b * y_laz + inv.c
            row = inv.d * x_laz + inv.e * y_laz + inv.f
            u = col / float(raster_width)
            v = row / float(raster_height)
            v = 1.0 - v
        else:
            x3857, y3857 = to_3857_from_laz.transform(x_laz, y_laz)
            u = (x3857 - xmin) / (xmax - xmin)
            v = (y3857 - ymin) / (ymax - ymin)
            v = 1.0 - v
        if cfg.naip_flip_u:
            u = 1.0 - u
        if cfg.naip_flip_v:
            v = 1.0 - v
        terrain_uv = list(zip(u, v))

    if mesh is not None:
        export_mesh(mesh, str(mesh_path))

    if cfg.export_terrain and terrain_mesh is not None:
        if cfg.naip_texture and terrain_uv is not None:
            export_obj_with_uv(
                terrain_mesh,
                terrain_uv,
                str(terrain_path),
                str(terrain_mtl_path),
                terrain_tex_path.name,
            )
            if cfg.combine_output and mesh is not None:
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

    if cfg.combine_output and not cfg.naip_texture and terrain_mesh is not None:
        if mesh is None:
            logger.warning("No combined mesh produced (missing buildings)")
        else:
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
        dxf_path = tile_dir / "contours.dxf"
        dxf = DxfExporter()

        # Transform function from WGS84 to LAZ CRS
        to_laz = Transformer.from_crs("EPSG:4326", laz_crs, always_xy=True)

        marker_center = None
        if lon is not None and lat is not None:
            try:
                cx, cy = to_laz.transform(lon, lat)
                marker_center = (cx * unit_scale, cy * unit_scale, 0.0)
            except Exception:
                marker_center = None
        elif cfg.clip_center_xy is not None:
            marker_center = (cfg.clip_center_xy[0], cfg.clip_center_xy[1], 0.0)

        if marker_center is not None:
            dxf.add_cross(marker_center, size=50.0, layer_name="origin")
            dxf.add_north_arrow(marker_center, layer_name="north")

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
            parcels_bbox = None
            if clip_bbox_wgs84:
                parcels_bbox = clip_bbox_wgs84
            elif tile_info and tile_info.get("bbox_wgs84"):
                bbox = tile_info["bbox_wgs84"]
                parcels_bbox = (
                    bbox["xmin"],
                    bbox["ymin"],
                    bbox["xmax"],
                    bbox["ymax"],
                )

            if parcels_bbox is None:
                logger.warning("No parcel bbox available; skipping parcel export.")
            else:
                source, parcels = fetch_parcels_for_bbox(parcels_bbox)
                if source is None or parcels is None:
                    logger.warning(
                        "No parcel source available for this area; skipping."
                    )
                else:
                    parcel_count = dxf.add_polygons_from_geojson(
                        parcels,
                        layer_name="PARCELS",
                        xy_scale=unit_scale,
                        transform_func=to_laz.transform,
                        color=3,  # Green
                    )
                    logger.info(
                        f"  Added {parcel_count} parcel boundaries ({source.name})"
                    )

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
        "job_id": job_id,
        "output_dir": str(tile_dir),
        "tile": tile_name,
        "provider": provider,
        "source_type": source_type_used
        or (tile_info.get("source_type", "laz") if tile_info else None),
        "coverage": {
            "status": tile_info.get("coverage_status") if tile_info else None,
            "ratio": tile_info.get("coverage_ratio") if tile_info else None,
            "source": tile_info.get("coverage_source") if tile_info else None,
        },
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
        "naip_tiled": naip_tiled_used if cfg.naip_texture else None,
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
    if cfg.cleanup_intermediates:
        _cleanup_intermediates(tile_dir)

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
    build.add_argument(
        "--provider",
        choices=["va", "national"],
        default="va",
        help="Data provider to use (va=VGIN, national=USGS 3DEP).",
    )
    build.add_argument(
        "--ept-only",
        action="store_true",
        help="National mode only: require EPT coverage and skip LAZ fallback.",
    )
    build.add_argument(
        "--prefer-ept",
        dest="prefer_ept",
        action="store_true",
        help="Prefer USGS EPT for point clouds (falls back to VGIN/LAZ).",
    )
    build.add_argument(
        "--no-prefer-ept",
        dest="prefer_ept",
        action="store_false",
        help="Disable EPT preference and use VGIN/LAZ directly.",
    )
    build.set_defaults(prefer_ept=True)
    build.add_argument("--out", type=Path, default=DEFAULT_OUT_DIR)
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
    build.add_argument("--naip-tiled", action="store_true")
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
    build.add_argument(
        "--no-buildings", action="store_true", help="Skip exporting buildings mesh."
    )
    build.add_argument(
        "--no-terrain", action="store_true", help="Skip exporting terrain mesh."
    )
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
            naip_tiled=args.naip_tiled,
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
            export_terrain=not args.no_terrain,
            prefer_ept=args.prefer_ept,
            flip_y=args.flip_y,
            flip_x=args.flip_x,
            terrain_flip_y=args.terrain_flip_y,
            rotate_z=args.rotate_z,
            provider=args.provider,
            ept_only=args.ept_only,
        )
        return build_command(cfg)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
