from __future__ import annotations

import json
import random
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, Iterable

from pyproj import CRS, Transformer
from shapely.geometry import box
from shapely.ops import transform as shp_transform

from ..config import BuildConfig
from ..core.geo import bbox_contains, bbox_from_center_wgs84
from ..core.heights import (
    FEET_PER_METER,
    derive_heights,
    get_laz_crs_wkt,
    get_unit_scale,
    reproject_features,
)
from ..core.mesh import (
    DxfExporter,
    apply_scene_transform,
    combine_meshes,
    export_contours_xyz,
    export_mesh,
    export_obj_with_uv,
    export_scene_with_terrain_texture,
    export_terrain_xyz,
    extrude_footprints,
    generate_contours_from_raster,
    resample_contours,
    terrain_mesh_from_raster,
)
from ..core.naip import download_naip_image, download_naip_image_tiled
from ..core.raster import (
    clip_raster,
    ept_to_laz,
    fill_nodata_raster,
    make_dsm,
    make_dtm,
    make_dtm_unclassified,
    make_ndsm,
    merge_lazs,
    raster_has_data,
)
from ..parcels.registry import fetch_parcels_for_bbox
from ..pipeline.io import (
    allocate_output_dir,
    cleanup_intermediates,
    generate_job_id,
    write_job_info,
)
from ..pipeline.report import write_report
from ..providers import (
    national_footprints,
    rockyweb_health,
    usgs_ept,
    usgs_index,
    usgs_laz,
    vgin,
)
from ..util import download_file, ensure_dir, get_logger, write_json

OUTPUT_CHOICES = {"buildings", "terrain", "contours", "parcels", "naip", "xyz"}


def _validate_outputs(outputs: Iterable[str]) -> set[str]:
    cleaned = []
    for value in outputs:
        if value is None:
            continue
        name = value.strip().lower()
        if not name:
            continue
        cleaned.append(name)

    if not cleaned:
        raise ValueError(
            "No outputs specified. Provide --outputs with at least one value."
        )

    unknown = [name for name in cleaned if name not in OUTPUT_CHOICES]
    if unknown:
        raise ValueError(
            "Unknown outputs: "
            + ", ".join(sorted(set(unknown)))
            + f" (valid: {', '.join(sorted(OUTPUT_CHOICES))})"
        )

    # Preserve order while de-duplicating
    result: list[str] = []
    seen: set[str] = set()
    for name in cleaned:
        if name in seen:
            continue
        result.append(name)
        seen.add(name)
    return set(result)


def _national_job_name(lat: float, lon: float, size: float | None, units: str) -> str:
    if size is None:
        return f"national_{lat:.5f}_{lon:.5f}"
    suffix = f"{size:g}{units[0]}"
    return f"national_{lat:.5f}_{lon:.5f}_{suffix}"


def _image_job_name(lat: float, lon: float, size: float, units: str) -> str:
    suffix = f"{size:g}{units[0]}"
    return f"image_{lat:.5f}_{lon:.5f}_{suffix}"


def build(cfg: BuildConfig) -> int:
    """Run the full build pipeline for a configuration."""

    logger = get_logger()
    provider = cfg.provider
    warnings: list[str] = []
    source_type_used: str | None = None
    naip_tiled_used: bool | None = cfg.naip_tiled

    outputs = _validate_outputs(cfg.outputs)
    export_buildings = "buildings" in outputs
    export_terrain = "terrain" in outputs
    export_contours = "contours" in outputs
    export_parcels = "parcels" in outputs
    export_naip = "naip" in outputs
    export_xyz = "xyz" in outputs
    include_parcels = export_parcels or cfg.dxf_include_parcels
    include_buildings = cfg.dxf_include_buildings

    if export_contours and cfg.contour_interval is None:
        raise ValueError("Contours output requires --contours INTERVAL.")
    if export_xyz and cfg.xyz_mode == "contours" and cfg.contour_interval is None:
        raise ValueError(
            "XYZ contour output requires --contours INTERVAL "
            "(even if 'contours' output is disabled). "
            "Use --xyz-mode grid for a full terrain grid."
        )
    if (
        not export_contours
        and cfg.contour_interval is not None
        and not (export_xyz and cfg.xyz_mode == "contours")
    ):
        raise ValueError("--contours requires 'contours' in --outputs.")
    if cfg.combine_output and not (export_buildings and export_terrain):
        raise ValueError(
            "--combine-output requires both buildings and terrain outputs."
        )

    lat, lon = None, None
    if cfg.center is not None:
        lat, lon = cfg.center

    if cfg.size is not None and (lat is None or lon is None):
        raise ValueError("Provide --center when using --size.")
    if (lat is not None or lon is not None) and cfg.size is None:
        raise ValueError("Provide --size when using --center.")

    clip_bbox_wgs84_hint = None
    if lat is not None and lon is not None and cfg.size is not None:
        clip_bbox_wgs84_hint = bbox_from_center_wgs84(lat, lon, cfg.size, cfg.units)

    image_only = outputs == {"naip"}

    tile_name = cfg.tile_name
    tile_info = None

    if image_only:
        if lat is None or lon is None or cfg.size is None:
            raise ValueError("Image-only output requires --center and --size.")
        if tile_name is None:
            tile_name = _image_job_name(lat, lon, cfg.size, cfg.units)
        job_id = cfg.job_id or generate_job_id((lat, lon), cfg.size, cfg.units)
        tile_dir, job_id = allocate_output_dir(
            cfg.out_dir, job_id, fixed_job_id=cfg.job_id is not None
        )
        write_job_info(
            tile_dir / "README.txt",
            tile_name=tile_name,
            job_id=job_id,
            provider=provider,
            lat=lat,
            lon=lon,
            clip_size=cfg.size,
            units=cfg.units,
            bbox_wgs84=None,
        )
        terrain_tex_path = tile_dir / "terrain.png"
        report_path = tile_dir / "report.json"

        logger.info("Stage 1/2: download NAIP image")
        size_m = cfg.size / FEET_PER_METER if cfg.units == "feet" else cfg.size
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
            "outputs": sorted(outputs),
            "clip": {
                "enabled": True,
                "center_latlon": (lat, lon),
                "size": cfg.size,
            },
            "naip": {
                "enabled": True,
                "pixel_size": cfg.naip_pixel_size,
                "max_size": cfg.naip_max_size,
                "tiled": naip_tiled_used,
            },
            "warnings": warnings,
        }
        write_report(report_path, report)
        if cfg.cleanup_intermediates:
            cleanup_intermediates(tile_dir)
        logger.info("Done (image-only)")
        return 0

    if provider == "va":
        if lat is not None and lon is not None and tile_name is None:
            logger.info("Looking up tile from coordinates...")
            tiles = vgin.tiles_for_point(lon, lat)
            if len(tiles) > 1:
                logger.warning(
                    "Multiple tiles found at this location: "
                    f"{[t['tile_name'] for t in tiles]}. Using first: {tiles[0]['tile_name']}"
                )
            tile_info = tiles[0]
            tile_name = tile_info["tile_name"]
            logger.info(f"Found tile: {tile_name}")

        if tile_name is None:
            raise ValueError("Either tile_name or --center must be provided")
    else:
        if lat is None or lon is None:
            raise ValueError("National provider requires --center coordinates")
        if tile_name is None:
            tile_name = _national_job_name(lat, lon, cfg.size, cfg.units)

    cache_dir = cfg.out_dir / "_cache"

    def _build_laz_fallback_tile_info() -> Dict[str, Any]:
        features = usgs_index.query_for_point(lon, lat)
        if not features:
            raise ValueError("No USGS LiDAR workunits found at this location")
        feature = usgs_index.select_best_feature(features)
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
        tile_info = vgin.tile_lookup(tile_name)
    else:
        if cfg.size is None:
            raise ValueError("National provider requires --size")
        ept_source = None
        if clip_bbox_wgs84_hint is not None:
            ept_source = usgs_ept.resolve_ept_from_bbox(
                clip_bbox_wgs84_hint, logger=logger, cache_dir=cache_dir
            )
        if ept_source is None:
            ept_source = usgs_ept.resolve_ept_from_point(
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

    job_center = None
    if lat is not None and lon is not None:
        job_center = (lat, lon)
    elif tile_info and tile_info.get("bbox_wgs84"):
        bbox = tile_info["bbox_wgs84"]
        job_center = (
            (bbox["ymin"] + bbox["ymax"]) / 2.0,
            (bbox["xmin"] + bbox["xmax"]) / 2.0,
        )

    job_id = cfg.job_id or generate_job_id(job_center, cfg.size, cfg.units)
    tile_dir, job_id = allocate_output_dir(
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
    combined_path = tile_dir / "combined.obj"
    combined_mtl_path = tile_dir / "combined.mtl"
    dtm_clip_path = tile_dir / "dtm_clip.tif"
    report_path = tile_dir / "report.json"
    merged_laz_path = tile_dir / "tiles_merged.laz"

    write_json(tile_json, tile_info)

    write_job_info(
        tile_dir / "README.txt",
        tile_name=tile_name,
        job_id=job_id,
        provider=provider,
        lat=lat,
        lon=lon,
        clip_size=cfg.size,
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
    tile_infos = [tile_info]
    laz_paths = [laz_path]
    laz_processing_path = laz_path
    multi_tile_used = False

    if provider == "va":
        use_ept = (
            cfg.prefer_ept
            and lat is not None
            and lon is not None
            and cfg.size is not None
        )
        if use_ept:
            ept_source = None
            if clip_bbox_wgs84_hint is not None:
                ept_source = usgs_ept.resolve_ept_from_bbox(
                    clip_bbox_wgs84_hint, logger=logger, cache_dir=cache_dir
                )
            if ept_source is None:
                ept_source = usgs_ept.resolve_ept_from_point(
                    lon, lat, logger=logger, cache_dir=cache_dir
                )
            if ept_source is not None and ept_source.crs_wkt:
                ept_crs = CRS.from_wkt(ept_source.crs_wkt)
                to_laz = Transformer.from_crs("EPSG:4326", ept_crs, always_xy=True)
                wgs_bb = clip_bbox_wgs84_hint or bbox_from_center_wgs84(
                    lat, lon, cfg.size, cfg.units
                )
                c1 = to_laz.transform(wgs_bb[0], wgs_bb[1])
                c2 = to_laz.transform(wgs_bb[2], wgs_bb[3])
                bounds = (
                    min(c1[0], c2[0]),
                    min(c1[1], c2[1]),
                    max(c1[0], c2[0]),
                    max(c1[1], c2[1]),
                )
                try:
                    ept_to_laz(ept_source.uri, laz_path, bounds)
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
            source_type_used = "laz"
    else:
        source_type = tile_info.get("source_type")
        if source_type == "ept":
            ept_url = tile_info.get("ept_url")
            ept_wkt = tile_info.get("crs_wkt")
            if not ept_url:
                raise ValueError("Missing EPT URL in tile info")
            if not ept_wkt:
                ept_source = usgs_ept.resolve_ept_from_point(
                    lon, lat, logger=logger, cache_dir=cache_dir
                )
                if ept_source is None or not ept_source.crs_wkt:
                    raise ValueError("Failed to resolve EPT CRS")
                ept_wkt = ept_source.crs_wkt
                tile_info["crs_wkt"] = ept_wkt
                write_json(tile_json, tile_info)
            ept_crs = CRS.from_wkt(ept_wkt)
            to_laz = Transformer.from_crs("EPSG:4326", ept_crs, always_xy=True)
            wgs_bb = clip_bbox_wgs84_hint or bbox_from_center_wgs84(
                lat, lon, cfg.size, cfg.units
            )
            c1 = to_laz.transform(wgs_bb[0], wgs_bb[1])
            c2 = to_laz.transform(wgs_bb[2], wgs_bb[3])
            bounds = (
                min(c1[0], c2[0]),
                min(c1[1], c2[1]),
                max(c1[0], c2[0]),
                max(c1[1], c2[1]),
            )
            try:
                if cfg.force or not laz_path.exists():
                    ept_to_laz(ept_url, laz_path, bounds)
                source_type_used = "ept"
            except Exception as exc:
                if cfg.ept_only:
                    raise
                msg = f"EPT fetch failed; falling back to LAZ ({exc})"
                logger.warning(msg)
                warnings.append(msg)
                tile_info = _build_laz_fallback_tile_info()
                write_json(tile_json, tile_info)
                source_type = "laz"
        if source_type == "laz":
            health = rockyweb_health.check_rockyweb(
                cache_dir / "rockyweb_health.json", logger=logger
            )
            if not health.get("ok"):
                raise ValueError(
                    "rockyweb is unavailable (EPT missing and LAZ fallback blocked). "
                    f"status={health.get('status')} error={health.get('error')}"
                )
            lpc_link = tile_info.get("lpc_link")
            if not lpc_link:
                raise ValueError("Missing LPC link for LAZ fallback")
            laz_urls = usgs_laz.list_laz_urls(lpc_link, logger=logger)
            if not laz_urls:
                raise ValueError("No LAZ URLs found for workunit")
            if cfg.size is None:
                raise ValueError("National provider requires --size")
            if clip_bbox_wgs84_hint is None:
                clip_bbox_wgs84_hint = bbox_from_center_wgs84(
                    lat, lon, cfg.size, cfg.units
                )
            cache_dir = cfg.out_dir / "_cache" / "usgs_laz"
            workunit = tile_info.get("workunit", "workunit")
            cache_path = cache_dir / f"{workunit}.json"
            tiles_index = usgs_laz.build_laz_index(
                laz_urls, cache_path, force=cfg.force, logger=logger
            )
            selected = usgs_laz.select_laz_tiles(tiles_index, clip_bbox_wgs84_hint)
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
            pass
        else:
            raise ValueError(
                f"Unknown source_type for national provider: {source_type}"
            )

    laz_wkt = get_laz_crs_wkt(str(laz_processing_path))
    laz_crs = CRS.from_wkt(laz_wkt)
    xy_scale = get_unit_scale(laz_crs, cfg.units, latitude=lat)
    z_scale = get_unit_scale(laz_crs, cfg.units, latitude=None)

    clip_poly = None
    clip_bbox_wgs84 = None

    # Center of the clip area in LAZ CRS, used to zero-origin all outputs
    center_laz_x: float | None = None
    center_laz_y: float | None = None

    if cfg.size is not None and lat is not None and lon is not None:
        if provider == "va":
            bbox = tile_info["bbox_wgs84"]
            if not (
                bbox["xmin"] <= lon <= bbox["xmax"]
                and bbox["ymin"] <= lat <= bbox["ymax"]
            ):
                raise ValueError(
                    f"Clip center ({lat}, {lon}) is outside the tile bbox."
                )

        to_laz = Transformer.from_crs("EPSG:4326", laz_crs, always_xy=True)
        cx, cy = to_laz.transform(lon, lat)
        center_laz_x, center_laz_y = cx, cy

        # Build the clip polygon by transforming the accurate WGS84 bbox
        # corners into LAZ CRS.  This avoids Mercator-scale distortion that
        # occurs when applying a metre offset directly in EPSG:3857.
        wgs84_bbox = clip_bbox_wgs84_hint
        if wgs84_bbox is None:
            wgs84_bbox = bbox_from_center_wgs84(lat, lon, cfg.size, cfg.units)
        corners_laz = [
            to_laz.transform(wgs84_bbox[0], wgs84_bbox[1]),
            to_laz.transform(wgs84_bbox[0], wgs84_bbox[3]),
            to_laz.transform(wgs84_bbox[2], wgs84_bbox[1]),
            to_laz.transform(wgs84_bbox[2], wgs84_bbox[3]),
        ]
        laz_xs = [c[0] for c in corners_laz]
        laz_ys = [c[1] for c in corners_laz]
        clip_poly = box(min(laz_xs), min(laz_ys), max(laz_xs), max(laz_ys))

        to_wgs84 = Transformer.from_crs(laz_crs, "EPSG:4326", always_xy=True)
        clip_poly_wgs84 = shp_transform(to_wgs84.transform, clip_poly)
        minx, miny, maxx, maxy = clip_poly_wgs84.bounds
        clip_bbox_wgs84 = (minx, miny, maxx, maxy)

    if clip_bbox_wgs84 is not None and provider == "va" and source_type_used != "ept":
        bbox = tile_info["bbox_wgs84"]
        spillover = not bbox_contains(bbox, clip_bbox_wgs84)
        if spillover and cfg.allow_multi_tile:
            logger.info("Clip extends beyond base tile; fetching intersecting tiles...")
            tile_infos = vgin.tiles_for_bbox(clip_bbox_wgs84)
            if not tile_infos:
                raise ValueError("No tiles found for clip bbox")

            tile_infos = sorted(
                tile_infos,
                key=lambda t: (
                    t.get("tile_name") != tile_name,
                    t.get("tile_name", ""),
                ),
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

    logger.info("Stage 3/6: fetch footprints")
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
            footprints = vgin.fetch_footprints_geojson(bbox_tuple)
        else:
            if clip_bbox_wgs84 is None:
                raise ValueError(
                    "National provider requires a clip bbox for footprints"
                )
            footprints = national_footprints.fetch_footprints_geojson(clip_bbox_wgs84)
        footprints_path.write_text(json.dumps(footprints))

    logger.info("Stage 4/6: generate rasters")
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

    needs_heights = export_buildings
    if needs_heights and not override_heights:
        if cfg.force or not dsm_path.exists():
            make_dsm(laz_processing_path, dsm_path, cfg.resolution)
        if cfg.force or not ndsm_path.exists():
            make_ndsm(dsm_path, dtm_use_path, ndsm_path)

    terrain_source_path = dtm_use_path
    if clip_poly is not None:
        if cfg.force or not dtm_clip_path.exists():
            clip_raster(dtm_use_path, dtm_clip_path, clip_poly)
        terrain_source_path = dtm_clip_path

    logger.info("Stage 5/6: compute heights")

    heights = []
    height_warnings: list[str] = []
    if needs_heights:
        min_height_laz = cfg.min_height / z_scale
        max_height_laz = cfg.max_height / z_scale
        floor_to_floor_laz = cfg.floor_to_floor / z_scale

        reprojected = reproject_features(footprints, laz_crs)
        if clip_poly is not None:
            reprojected = [
                f for f in reprojected if f["geometry"].intersects(clip_poly)
            ]
        if not reprojected:
            logger.warning("No footprints intersect the clip area after reprojection")

        override_range = None
        rng = None
        if override_heights:
            if cfg.random_heights_min >= cfg.random_heights_max:
                raise ValueError("random-heights min must be < max")
            override_range = (
                cfg.random_heights_min / z_scale,
                cfg.random_heights_max / z_scale,
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

    logger.info("Stage 6/6: mesh export")
    mesh = None
    if export_buildings:
        mesh = extrude_footprints(heights, xy_scale=xy_scale, z_scale=z_scale)
        if mesh is None:
            logger.warning("No mesh produced (empty footprints or extrusion failures)")

    terrain_mesh = None
    terrain_uv = None
    if export_terrain:
        terrain_mesh = terrain_mesh_from_raster(
            str(terrain_source_path),
            xy_scale=xy_scale,
            z_scale=z_scale,
            sample=cfg.terrain_sample,
        )
        if terrain_mesh is None:
            logger.warning("No terrain mesh produced (empty or invalid DTM)")

    uv_context = None
    if export_naip:
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
        apply_scene_transform(terrain_mesh, center_x, center_y, flip_y=True)

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

    if (
        export_naip
        and export_terrain
        and terrain_mesh is not None
        and uv_context is not None
    ):
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
        x_laz = verts[:, 0] / xy_scale
        y_laz = verts[:, 1] / xy_scale
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

    if export_terrain and terrain_mesh is not None:
        if export_naip and terrain_uv is not None:
            export_obj_with_uv(
                terrain_mesh,
                terrain_uv,
                str(terrain_path),
                str(terrain_mtl_path),
                terrain_tex_path.name,
            )
            if cfg.combine_output and mesh is not None:
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

    if cfg.combine_output and not export_naip and terrain_mesh is not None:
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

    # Origin offset in scaled output units – centres all DXF/XYZ output on
    # the user's --center point so coordinates are small, relative values.
    dxf_origin: tuple[float, float] | None = None
    if center_laz_x is not None and center_laz_y is not None:
        dxf_origin = (center_laz_x * xy_scale, center_laz_y * xy_scale)

    contours = None
    contours_needed = export_contours or (export_xyz and cfg.xyz_mode == "contours")
    if contours_needed and cfg.contour_interval is not None:
        interval_laz = cfg.contour_interval / z_scale
        contours = generate_contours_from_raster(
            str(terrain_source_path),
            interval=interval_laz,
            xy_scale=xy_scale,
            z_scale=z_scale,
            sample=1,
            origin=dxf_origin,
            rotate_deg=cfg.rotate_z,
        )

    xyz_point_count = 0
    if export_xyz:
        xyz_path = tile_dir / "terrain.xyz"
        if cfg.xyz_mode == "contours":
            if contours:
                spacing = cfg.xyz_contour_spacing or 0.0
                xyz_point_count = export_contours_xyz(
                    contours, str(xyz_path), spacing=spacing
                )
        else:
            xyz_point_count = export_terrain_xyz(
                str(terrain_source_path),
                str(xyz_path),
                xy_scale=xy_scale,
                z_scale=z_scale,
                sample=cfg.terrain_sample,
                origin=dxf_origin,
                rotate_deg=cfg.rotate_z,
            )
        logger.info(f"Exported {xyz_point_count} points to {xyz_path}")

    export_dxf = export_contours or include_parcels
    if export_dxf:
        logger.info("Generating DXF export")
        dxf_path = tile_dir / "contours.dxf"
        dxf = DxfExporter()

        to_laz = Transformer.from_crs("EPSG:4326", laz_crs, always_xy=True)

        marker_center = (0.0, 0.0, 0.0)
        if lat is not None and lon is not None and dxf_origin is None:
            try:
                cx, cy = to_laz.transform(lon, lat)
                marker_center = (cx * xy_scale, cy * xy_scale, 0.0)
            except Exception:
                pass

        dxf.add_cross(marker_center, size=50.0, layer_name="origin")
        dxf.add_north_arrow(marker_center, layer_name="north")

        if export_contours and contours:
            dxf_contours = contours
            if cfg.dxf_contour_spacing:
                dxf_contours = resample_contours(contours, cfg.dxf_contour_spacing)
            major_interval = cfg.contour_interval * 5
            contour_count = dxf.add_contours(
                dxf_contours, major_interval=major_interval
            )
            logger.info(f"  Added {contour_count} contour polylines")

        if include_parcels:
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
                        xy_scale=xy_scale,
                        transform_func=to_laz.transform,
                        color=3,
                        origin=dxf_origin,
                        clip_boundary=clip_poly,
                        rotate_deg=cfg.rotate_z,
                    )
                    logger.info(
                        f"  Added {parcel_count} parcel boundaries ({source.name})"
                    )

        if include_buildings:
            building_count = dxf.add_polygons_from_geojson(
                footprints,
                layer_name="BUILDINGS",
                xy_scale=xy_scale,
                transform_func=to_laz.transform,
                color=5,
                origin=dxf_origin,
                clip_boundary=clip_poly,
                rotate_deg=cfg.rotate_z,
            )
            logger.info(f"  Added {building_count} building footprints")

        dxf.save(str(dxf_path))
        logger.info(f"Exported DXF to {dxf_path}")

    if not cfg.keep_rasters:
        for path in (dtm_path, dtm_filled_path, dtm_clip_path, dsm_path, ndsm_path):
            if path.exists():
                path.unlink()

    height_values = [h.height * z_scale for h in heights]
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
        "unit_scale": xy_scale,
        "xy_scale": xy_scale,
        "z_scale": z_scale,
        "outputs": sorted(outputs),
        "footprints_total": len(footprints.get("features", [])),
        "footprints_extruded": len(heights) if needs_heights else 0,
        "clip": {
            "enabled": clip_poly is not None,
            "center_latlon": (lat, lon)
            if lat is not None and lon is not None
            else None,
            "size": cfg.size,
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
        "naip": {
            "enabled": export_naip,
            "pixel_size": cfg.naip_pixel_size if export_naip else None,
            "max_size": cfg.naip_max_size if export_naip else None,
            "tiled": naip_tiled_used if export_naip else None,
            "flip_u": cfg.naip_flip_u if export_naip else None,
            "flip_v": cfg.naip_flip_v if export_naip else None,
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
        }
        if needs_heights
        else None,
        "contours": {
            "enabled": export_contours,
            "interval": cfg.contour_interval if export_contours else None,
            "dxf_spacing": cfg.dxf_contour_spacing if export_contours else None,
            "include_parcels": include_parcels if export_dxf else None,
            "include_buildings": include_buildings if export_dxf else None,
        },
        "xyz": {
            "enabled": export_xyz,
            "points": xyz_point_count if export_xyz else None,
            "mode": cfg.xyz_mode if export_xyz else None,
            "contour_interval": cfg.contour_interval
            if export_xyz and cfg.xyz_mode == "contours"
            else None,
            "contour_spacing": cfg.xyz_contour_spacing
            if export_xyz and cfg.xyz_mode == "contours"
            else None,
        },
        "warnings": warnings,
    }
    write_report(report_path, report)
    if cfg.cleanup_intermediates:
        cleanup_intermediates(tile_dir)

    logger.info("Done")
    return 0
