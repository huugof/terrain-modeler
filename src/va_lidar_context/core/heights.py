from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import laspy
import numpy as np
import tifffile
from matplotlib.path import Path as MplPath
from pyproj import CRS, Transformer
from shapely.geometry import MultiPolygon, Polygon, shape
from shapely.ops import transform

from .raster import RasterMeta, load_raster_meta, world_to_pixel

FEET_PER_METER = 3.28084


@dataclass
class FootprintHeight:
    geometry: Any
    height: float
    source: str
    base_z: float = 0.0


def get_laz_crs_wkt(laz_path: str) -> str:
    """Read LAZ CRS WKT from laspy metadata."""
    las = laspy.read(laz_path)
    parsed = las.header.parse_crs()
    if parsed is not None:
        try:
            return parsed.to_wkt()
        except Exception:
            pass
    for vlr in las.header.vlrs:
        if getattr(vlr, "string", None):
            text = str(vlr.string).strip()
            if "GEOGCS" in text or "PROJCRS" in text or "COMPD_CS" in text:
                return text
        raw = getattr(vlr, "record_data", None)
        if isinstance(raw, bytes):
            text = raw.decode("utf-8", errors="ignore").strip()
            if "GEOGCS" in text or "PROJCRS" in text or "COMPD_CS" in text:
                return text
    raise ValueError("LAZ CRS not found in header metadata")


def get_unit_scale(crs: CRS, output_units: str, latitude: float | None = None) -> float:
    """Return a multiplier to convert CRS units to desired output units.

    When *latitude* is provided and the CRS is Web Mercator (EPSG:3857),
    the scale is corrected for Mercator distortion so that output
    coordinates represent true ground distances.
    """
    import math

    axis = crs.axis_info[0] if crs.axis_info else None
    to_meters = (
        axis.unit_conversion_factor if axis and axis.unit_conversion_factor else 1.0
    )
    # Web Mercator metres are not true metres — correct with cos(lat).
    if latitude is not None:
        try:
            epsg = crs.to_epsg()
        except Exception:
            epsg = None
        if epsg == 3857:
            to_meters *= math.cos(math.radians(latitude))
    if output_units == "meters":
        return to_meters
    if output_units == "feet":
        return to_meters * FEET_PER_METER
    raise ValueError(f"Unsupported units: {output_units}")


def reproject_features(
    geojson: Dict[str, Any],
    dst_crs: CRS,
    src_crs: CRS | str = "EPSG:4326",
) -> List[Dict[str, Any]]:
    """Reproject GeoJSON features into the target CRS."""
    transformer = Transformer.from_crs(src_crs, dst_crs, always_xy=True)

    def _transform_geom(geom):
        return transform(transformer.transform, geom)

    features = []
    for feat in geojson.get("features", []):
        geom = shape(feat.get("geometry"))
        if geom.is_empty:
            continue
        geom = _transform_geom(geom)
        features.append(
            {
                "geometry": geom,
                "properties": feat.get("properties", {}),
            }
        )
    return features


def _polygon_contains_points(polygon, points: np.ndarray) -> np.ndarray:
    def _contains_poly(poly: Polygon, pts: np.ndarray) -> np.ndarray:
        exterior = MplPath(np.asarray(poly.exterior.coords))
        inside = exterior.contains_points(pts)
        for ring in poly.interiors:
            hole = MplPath(np.asarray(ring.coords))
            inside &= ~hole.contains_points(pts)
        return inside

    if isinstance(polygon, Polygon):
        return _contains_poly(polygon, points)
    if isinstance(polygon, MultiPolygon):
        inside = np.zeros(points.shape[0], dtype=bool)
        for poly in polygon.geoms:
            inside |= _contains_poly(poly, points)
        return inside
    return np.zeros(points.shape[0], dtype=bool)


def sample_raster_values(
    raster_path: str,
    polygon,
    raster_meta: RasterMeta | None = None,
) -> np.ndarray:
    """Sample raster values within a polygon footprint."""
    path = raster_path
    meta = raster_meta or load_raster_meta(Path(path))
    data = tifffile.imread(path)
    if data.ndim == 3:
        data = data[0]
    data = np.asarray(data, dtype=np.float32)
    nodata = float(meta.nodata)

    minx, miny, maxx, maxy = polygon.bounds
    bbox_cols: list[float] = []
    bbox_rows: list[float] = []
    for x, y in ((minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)):
        col, row = world_to_pixel(meta.transform, x, y)
        bbox_cols.append(float(col))
        bbox_rows.append(float(row))

    col_min = max(0, int(np.floor(min(bbox_cols))) - 1)
    row_min = max(0, int(np.floor(min(bbox_rows))) - 1)
    col_max = min(meta.width, int(np.ceil(max(bbox_cols))) + 2)
    row_max = min(meta.height, int(np.ceil(max(bbox_rows))) + 2)

    if col_min >= col_max or row_min >= row_max:
        return np.array([], dtype=np.float32)

    crop = data[row_min:row_max, col_min:col_max]
    a, b, c, d, e, f = meta.transform
    cols = np.arange(col_min, col_max, dtype=np.float64) + 0.5
    rows = np.arange(row_min, row_max, dtype=np.float64) + 0.5
    col_grid, row_grid = np.meshgrid(cols, rows)
    xs = a * col_grid + b * row_grid + c
    ys = d * col_grid + e * row_grid + f
    points = np.column_stack((xs.ravel(), ys.ravel()))
    inside = _polygon_contains_points(polygon, points).reshape(crop.shape)
    values = crop[inside]
    values = values[(values != nodata) & np.isfinite(values)]
    return values


def compute_height(
    values: np.ndarray,
    percentile: int,
    min_height: float,
    max_height: float,
) -> Optional[float]:
    """Compute a clamped percentile height from raster samples."""
    if values.size == 0:
        return None
    h = float(np.percentile(values, percentile))
    return float(max(min_height, min(max_height, h)))


def compute_base(values: np.ndarray) -> Optional[float]:
    """Compute a base elevation using the median of raster samples."""
    if values.size == 0:
        return None
    return float(np.percentile(values, 50))


def fallback_height(
    properties: Dict[str, Any], floor_to_floor: float
) -> Optional[Tuple[float, str]]:
    """Fallback to attribute-derived heights when raster samples are missing."""
    if properties.get("BLDGHEIGHT") is not None:
        try:
            return float(properties["BLDGHEIGHT"]), "BLDGHEIGHT"
        except (TypeError, ValueError):
            pass
    if properties.get("NUMSTORIES") is not None:
        try:
            return float(properties["NUMSTORIES"]) * floor_to_floor, "NUMSTORIES"
        except (TypeError, ValueError):
            pass
    return None


def derive_heights(
    ndsm_path: str | None,
    dtm_path: str,
    ndsm_meta: RasterMeta | None,
    dtm_meta: RasterMeta | None,
    features: Iterable[Dict[str, Any]],
    percentile: int,
    min_height: float,
    max_height: float,
    floor_to_floor: float,
    override_height_range: Tuple[float, float] | None = None,
    rng: random.Random | None = None,
) -> Tuple[List[FootprintHeight], List[str]]:
    """Derive per-footprint heights and return any warnings."""
    results: List[FootprintHeight] = []
    warnings: List[str] = []

    if override_height_range and rng is None:
        rng = random.Random()

    for feat in features:
        geom = feat["geometry"]
        props = feat.get("properties", {})
        if override_height_range is None and ndsm_path is None:
            raise RuntimeError("nDSM path is required when not overriding heights")

        base_values = sample_raster_values(dtm_path, geom, raster_meta=dtm_meta)

        base_z = compute_base(base_values)
        if base_z is None:
            base_z = 0.0
            warnings.append("No DTM samples for footprint; using base_z=0")

        if override_height_range is not None:
            h = rng.uniform(override_height_range[0], override_height_range[1])
            results.append(
                FootprintHeight(
                    geometry=geom,
                    height=h,
                    source="RANDOM",
                    base_z=base_z,
                )
            )
            continue

        ndsm_values = sample_raster_values(ndsm_path, geom, raster_meta=ndsm_meta)
        height = compute_height(ndsm_values, percentile, min_height, max_height)
        if height is not None:
            results.append(
                FootprintHeight(
                    geometry=geom,
                    height=height,
                    source=f"P{percentile}",
                    base_z=base_z,
                )
            )
            continue

        fallback = fallback_height(props, floor_to_floor)
        if fallback:
            h, source = fallback
            h = float(max(min_height, min(max_height, h)))
            results.append(
                FootprintHeight(
                    geometry=geom,
                    height=h,
                    source=source,
                    base_z=base_z,
                )
            )
            continue

        warnings.append("No height samples and no fallback attributes")

    return results, warnings
