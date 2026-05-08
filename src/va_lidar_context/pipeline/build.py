from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from pyproj import CRS, Transformer
from shapely.geometry import box

from ..config import BuildConfig
from ..core.geo import (
    FEET_PER_METER,
    bbox_from_center_wgs84,
    get_unit_scale,
)
from ..core.mesh import (
    DxfExporter,
    export_contours_xyz,
    export_terrain_xyz,
    generate_contours_from_raster,
    resample_contours,
)
from ..core.naip import download_naip_image, download_naip_image_tiled
from ..core.raster import clip_raster, fill_nodata_raster
from ..parcels.registry import fetch_parcels_for_bbox
from ..pipeline.io import (
    allocate_output_dir,
    cleanup_intermediates,
    generate_job_id,
    write_job_info,
)
from ..pipeline.types import BuildResult
from ..providers import national_footprints, usgs_3dep, vgin
from ..util import get_logger

OUTPUT_CHOICES = {"buildings", "terrain", "contours", "parcels", "naip", "xyz"}


def parse_outputs(
    value: str | None, default: tuple[str, ...] = ("contours", "naip", "xyz")
) -> tuple[str, ...]:
    """Parse and validate a comma-separated outputs string."""
    if value is None:
        return default
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
    seen: set[str] = set()
    result: list[str] = []
    for v in cleaned:
        if v not in seen:
            result.append(v)
            seen.add(v)
    return tuple(result)


def _validate_outputs(outputs: Iterable[str]) -> set[str]:
    return set(parse_outputs(",".join(str(o) for o in outputs if o is not None)))


def _national_job_name(lat: float, lon: float, size: float | None, units: str) -> str:
    if size is None:
        return f"national_{lat:.5f}_{lon:.5f}"
    suffix = f"{size:g}{units[0]}"
    return f"national_{lat:.5f}_{lon:.5f}_{suffix}"


def _image_job_name(lat: float, lon: float, size: float, units: str) -> str:
    suffix = f"{size:g}{units[0]}"
    return f"image_{lat:.5f}_{lon:.5f}_{suffix}"


# ---------------------------------------------------------------------------
# Stage helpers
# ---------------------------------------------------------------------------


def _stage_image_only(
    cfg: BuildConfig,
    lat: float,
    lon: float,
    outputs: set[str],
    warnings: List[str],
    naip_tiled_used: Optional[bool],
) -> BuildResult:
    """Fast-path for image-only (naip) jobs. Returns a completed BuildResult."""
    logger = get_logger()
    tile_name = cfg.tile_name or _image_job_name(lat, lon, cfg.size, cfg.units)
    job_id = cfg.job_id or generate_job_id((lat, lon), cfg.size, cfg.units)
    tile_dir, job_id = allocate_output_dir(cfg.out_dir, job_id, fixed_job_id=cfg.job_id is not None)
    write_job_info(
        tile_dir / "README.txt",
        tile_name=tile_name,
        job_id=job_id,
        provider=cfg.provider,
        lat=lat,
        lon=lon,
        clip_size=cfg.size,
        units=cfg.units,
        bbox_wgs84=None,
    )
    terrain_tex_path = tile_dir / "terrain.png"
    report_path = tile_dir / "report.json"
    preview_mesh_path = tile_dir / "preview.obj"

    logger.info("Stage 1/2: download NAIP image")
    size_m = cfg.size / FEET_PER_METER if cfg.units == "feet" else cfg.size
    half = size_m / 2.0
    to_merc = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
    cx, cy = to_merc.transform(lon, lat)
    bbox_3857 = (cx - half, cy - half, cx + half, cy + half)
    naip_tiled_used = _stage_download_naip(cfg, bbox_3857, terrain_tex_path, warnings)
    _write_preview_plane_obj(preview_mesh_path, cfg.size or 100.0)

    report: Dict[str, Any] = {
        "job_id": job_id,
        "output_dir": str(tile_dir),
        "tile": tile_name,
        "provider": cfg.provider,
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
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True))
    if cfg.cleanup_intermediates:
        cleanup_intermediates(tile_dir)
    logger.info("Done (image-only)")
    return BuildResult(exit_code=0, output_dir=tile_dir)


def _write_preview_plane_obj(path: Path, size: float) -> None:
    """Write a simple flat OBJ plane for fallback wireframe preview."""
    half = max(float(size) / 2.0, 1.0)
    path.write_text(
        "\n".join(
            [
                "# fallback preview plane",
                f"v {-half:.6f} {-half:.6f} 0.000000",
                f"v {half:.6f} {-half:.6f} 0.000000",
                f"v {half:.6f} {half:.6f} 0.000000",
                f"v {-half:.6f} {half:.6f} 0.000000",
                "f 1 2 3",
                "f 1 3 4",
                "",
            ]
        ),
        encoding="utf-8",
    )


def _stage_download_naip(
    cfg: BuildConfig,
    bbox_3857: Tuple[float, float, float, float],
    terrain_tex_path: Path,
    warnings: List[str],
) -> bool:
    """Download NAIP imagery. Returns whether tiled mode was used."""
    logger = get_logger()
    naip_tiled_used = cfg.naip_tiled
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
    return naip_tiled_used


def _stage_dxf_export(
    cfg: BuildConfig,
    tile_dir: Path,
    data_crs: Any,
    clip_poly: Any,
    clip_bbox_wgs84: Optional[Tuple[float, float, float, float]],
    contours: Any,
    dxf_origin: Optional[Tuple[float, float]],
    xy_scale: float,
    lat: Optional[float],
    lon: Optional[float],
    export_contours: bool,
    include_parcels: bool,
    include_buildings: bool,
    footprints: Dict[str, Any],
) -> None:
    """Export DXF file (contours, parcels, buildings)."""
    logger = get_logger()
    dxf_path = tile_dir / "contours.dxf"
    dxf = DxfExporter()

    to_data_crs = Transformer.from_crs("EPSG:4326", data_crs, always_xy=True)

    marker_center = (0.0, 0.0, 0.0)
    if lat is not None and lon is not None and dxf_origin is None:
        try:
            cx, cy = to_data_crs.transform(lon, lat)
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
        contour_count = dxf.add_contours(dxf_contours, major_interval=major_interval)
        logger.info(f"  Added {contour_count} contour polylines")

    if include_parcels and clip_bbox_wgs84 is not None:
        source, parcels = fetch_parcels_for_bbox(clip_bbox_wgs84)
        if source is None or parcels is None:
            logger.warning("No parcel source available for this area; skipping.")
        else:
            parcel_count = dxf.add_polygons_from_geojson(
                parcels,
                layer_name="PARCELS",
                xy_scale=xy_scale,
                transform_func=to_data_crs.transform,
                color=3,
                origin=dxf_origin,
                clip_boundary=clip_poly,
                rotate_deg=cfg.rotate_z,
            )
            logger.info(f"  Added {parcel_count} parcel boundaries ({source.name})")

    if include_buildings:
        building_count = dxf.add_polygons_from_geojson(
            footprints,
            layer_name="BUILDINGS",
            xy_scale=xy_scale,
            transform_func=to_data_crs.transform,
            color=5,
            origin=dxf_origin,
            clip_boundary=clip_poly,
            rotate_deg=cfg.rotate_z,
        )
        logger.info(f"  Added {building_count} building footprints")

    dxf.save(str(dxf_path))
    logger.info(f"Exported DXF to {dxf_path}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def build(cfg: BuildConfig) -> BuildResult:
    """Run the full build pipeline for a configuration."""

    logger = get_logger()
    warnings: list[str] = []
    naip_tiled_used: bool | None = cfg.naip_tiled

    outputs = _validate_outputs(cfg.outputs)
    export_contours = "contours" in outputs
    export_naip = "naip" in outputs
    export_xyz = "xyz" in outputs
    export_parcels = "parcels" in outputs
    include_parcels = export_parcels or cfg.dxf_include_parcels
    include_buildings = cfg.dxf_include_buildings
    needs_dtm = export_contours or export_xyz

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

    lat, lon = None, None
    if cfg.center is not None:
        lat, lon = cfg.center

    if cfg.size is not None and (not math.isfinite(cfg.size) or cfg.size <= 0):
        raise ValueError("--size must be a finite number greater than 0.")
    if cfg.size is not None and (lat is None or lon is None):
        raise ValueError("Provide --center when using --size.")
    if (lat is not None or lon is not None) and cfg.size is None:
        raise ValueError("Provide --size when using --center.")

    if lat is None or lon is None or cfg.size is None:
        raise ValueError("--center and --size are required.")

    clip_bbox_wgs84 = bbox_from_center_wgs84(lat, lon, cfg.size, cfg.units)
    image_only = outputs == {"naip"}

    if image_only:
        return _stage_image_only(cfg, lat, lon, outputs, warnings, naip_tiled_used)

    cache_dir = cfg.out_dir / "_cache"
    tile_name = cfg.tile_name or _national_job_name(lat, lon, cfg.size, cfg.units)
    job_id = cfg.job_id or generate_job_id((lat, lon), cfg.size, cfg.units)
    tile_dir, job_id = allocate_output_dir(cfg.out_dir, job_id, fixed_job_id=cfg.job_id is not None)

    dtm_path = tile_dir / "dtm.tif"
    dtm_filled_path = tile_dir / "dtm_filled.tif"
    footprints_path = tile_dir / "footprints.geojson"
    terrain_tex_path = tile_dir / "terrain.png"
    preview_mesh_path = tile_dir / "preview.obj"
    report_path = tile_dir / "report.json"

    write_job_info(
        tile_dir / "README.txt",
        tile_name=tile_name,
        job_id=job_id,
        provider=cfg.provider,
        lat=lat,
        lon=lon,
        clip_size=cfg.size,
        units=cfg.units,
        bbox_wgs84=None,
    )

    # Stage 1: fetch DTM from USGS 3DEP (only when needed for contours/XYZ)
    data_crs = None
    xy_scale = 1.0
    z_scale = 1.0
    clip_poly = None
    center_x = None
    center_y = None
    terrain_source_path = None
    contour_source_path = None

    if needs_dtm:
        logger.info("Stage 1/4: fetch terrain (USGS 3DEP)")
        dtm_raw_cache, data_crs = usgs_3dep.fetch_dtm(clip_bbox_wgs84, cache_dir, cfg.resolution)

        to_utm = Transformer.from_crs("EPSG:4326", data_crs, always_xy=True)
        center_x, center_y = to_utm.transform(lon, lat)

        xmin, ymin, xmax, ymax = clip_bbox_wgs84
        corners_utm = [
            to_utm.transform(xmin, ymin),
            to_utm.transform(xmin, ymax),
            to_utm.transform(xmax, ymin),
            to_utm.transform(xmax, ymax),
        ]
        xs = [c[0] for c in corners_utm]
        ys = [c[1] for c in corners_utm]
        clip_poly = box(min(xs), min(ys), max(xs), max(ys))

        clip_raster(dtm_raw_cache, dtm_path, clip_poly)

        dtm_use_path = dtm_path
        if cfg.fill_dtm:
            fill_nodata_raster(
                dtm_path,
                dtm_filled_path,
                max_distance=cfg.fill_max_dist,
                smoothing_iterations=cfg.fill_smoothing,
                hard_fill=cfg.fill_hard,
            )
            dtm_use_path = dtm_filled_path

        terrain_source_path = dtm_use_path
        contour_source_path = dtm_use_path

        xy_scale = get_unit_scale(data_crs, cfg.units, latitude=lat)
        z_scale = get_unit_scale(data_crs, cfg.units, latitude=None)
    else:
        # For parcels/naip-only jobs, still need a CRS for DXF projection
        from ..providers.usgs_3dep import _utm_epsg
        data_crs = CRS.from_epsg(_utm_epsg(lat, lon))
        to_utm = Transformer.from_crs("EPSG:4326", data_crs, always_xy=True)
        center_x, center_y = to_utm.transform(lon, lat)
        xmin, ymin, xmax, ymax = clip_bbox_wgs84
        corners_utm = [
            to_utm.transform(xmin, ymin),
            to_utm.transform(xmin, ymax),
            to_utm.transform(xmax, ymin),
            to_utm.transform(xmax, ymax),
        ]
        xs = [c[0] for c in corners_utm]
        ys = [c[1] for c in corners_utm]
        clip_poly = box(min(xs), min(ys), max(xs), max(ys))
        xy_scale = get_unit_scale(data_crs, cfg.units, latitude=lat)
        z_scale = get_unit_scale(data_crs, cfg.units, latitude=None)

    # Stage 2: fetch footprints
    logger.info("Stage 2/4: fetch footprints")
    if footprints_path.exists() and not cfg.force:
        footprints = json.loads(footprints_path.read_text())
    else:
        if cfg.provider == "va":
            footprints = vgin.fetch_footprints_geojson(clip_bbox_wgs84)
        else:
            footprints = national_footprints.fetch_footprints_geojson(clip_bbox_wgs84)
        footprints_path.write_text(json.dumps(footprints))

    # Stage 3: NAIP imagery
    if export_naip:
        logger.info("Stage 3/4: download NAIP")
        to_3857 = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
        xmin, ymin, xmax, ymax = clip_bbox_wgs84
        x1, y1 = to_3857.transform(xmin, ymin)
        x2, y2 = to_3857.transform(xmax, ymax)
        bbox_3857 = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        naip_tiled_used = _stage_download_naip(cfg, bbox_3857, terrain_tex_path, warnings)

    # Stage 4: contours, XYZ, DXF
    logger.info("Stage 4/4: export outputs")
    dxf_origin: tuple[float, float] | None = None
    if center_x is not None and center_y is not None:
        dxf_origin = (center_x * xy_scale, center_y * xy_scale)

    contours = None
    contours_needed = export_contours or (export_xyz and cfg.xyz_mode == "contours")
    if contours_needed and cfg.contour_interval is not None and contour_source_path is not None:
        interval_in_crs = cfg.contour_interval / z_scale
        contours = generate_contours_from_raster(
            str(contour_source_path),
            interval=interval_in_crs,
            xy_scale=xy_scale,
            z_scale=z_scale,
            sample=1,
            origin=dxf_origin,
            rotate_deg=cfg.rotate_z,
        )

    xyz_point_count = 0
    if export_xyz and terrain_source_path is not None:
        xyz_path = tile_dir / "terrain.xyz"
        if cfg.xyz_mode == "contours":
            if contours:
                spacing = cfg.xyz_contour_spacing or 0.0
                xyz_point_count = export_contours_xyz(contours, str(xyz_path), spacing=spacing)
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
        _stage_dxf_export(
            cfg,
            tile_dir,
            data_crs,
            clip_poly,
            clip_bbox_wgs84,
            contours,
            dxf_origin,
            xy_scale,
            lat,
            lon,
            export_contours,
            include_parcels,
            include_buildings,
            footprints,
        )

    # Write preview plane (no OBJ terrain mesh)
    _write_preview_plane_obj(preview_mesh_path, cfg.size or 100.0)

    # Clean up intermediate rasters
    if not cfg.keep_rasters:
        for path in (dtm_path, dtm_filled_path):
            if path.exists():
                path.unlink()

    report: Dict[str, Any] = {
        "job_id": job_id,
        "output_dir": str(tile_dir),
        "tile": tile_name,
        "provider": cfg.provider,
        "source_type": "3dep_cog",
        "units": cfg.units,
        "xy_scale": xy_scale,
        "z_scale": z_scale,
        "outputs": sorted(outputs),
        "footprints_total": len(footprints.get("features", [])),
        "clip": {
            "enabled": True,
            "center_latlon": (lat, lon),
            "size": cfg.size,
        },
        "transform": {
            "flip_x": cfg.flip_x,
            "flip_y": cfg.flip_y,
            "rotate_z": cfg.rotate_z,
        },
        "naip": {
            "enabled": export_naip,
            "pixel_size": cfg.naip_pixel_size if export_naip else None,
            "max_size": cfg.naip_max_size if export_naip else None,
            "tiled": naip_tiled_used if export_naip else None,
        },
        "dtm": {
            "source": "usgs_3dep",
            "resolution": cfg.resolution,
            "filled": cfg.fill_dtm,
        },
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
        },
        "warnings": warnings,
    }
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True))
    if cfg.cleanup_intermediates:
        cleanup_intermediates(tile_dir)

    logger.info("Done")
    return BuildResult(exit_code=0, output_dir=tile_dir)
