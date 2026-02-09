from __future__ import annotations

import json
import random
import subprocess
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import numpy as np
except Exception:  # pragma: no cover
    np = None

try:
    import rasterio
    from rasterio.mask import mask
except Exception:  # pragma: no cover
    rasterio = None
    mask = None

try:
    from pyproj import CRS, Transformer
except Exception:  # pragma: no cover
    CRS = None
    Transformer = None

try:
    from shapely.geometry import shape
    from shapely.ops import transform
except Exception:  # pragma: no cover
    shape = None
    transform = None


FEET_PER_METER = 3.28084


@dataclass
class FootprintHeight:
    geometry: Any
    height: float
    source: str
    base_z: float = 0.0


def get_laz_crs_wkt(laz_path: str) -> str:
    """Read LAZ CRS WKT from PDAL metadata."""
    proc = subprocess.run(
        ["pdal", "info", "--metadata", laz_path],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)
    srs = data.get("metadata", {}).get("srs", {})
    wkt = (
        srs.get("wkt")
        or srs.get("compoundwkt")
        or srs.get("comp_spatialreference")
        or srs.get("proj4")
    )
    if not wkt:
        raise ValueError("LAZ CRS not found in PDAL metadata")
    return wkt


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
    if Transformer is None or shape is None or transform is None:
        raise RuntimeError("pyproj and shapely are required for reprojection")
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


def sample_raster_values(raster_path: str, polygon) -> np.ndarray:
    """Sample raster values within a polygon footprint."""
    if rasterio is None or mask is None:
        raise RuntimeError("rasterio is required for raster sampling")
    with rasterio.open(raster_path) as ds:
        nodata = ds.nodata if ds.nodata is not None else -9999
        try:
            out_image, _ = mask(ds, [polygon], crop=True, all_touched=False)
        except ValueError:
            # Polygon doesn't overlap raster (e.g., building outside clip region)
            return np.array([])
        data = out_image[0]
        values = data[(data != nodata) & np.isfinite(data)]
        return values


def compute_height(
    values: np.ndarray,
    percentile: int,
    min_height: float,
    max_height: float,
) -> Optional[float]:
    """Compute a clamped percentile height from raster samples."""
    if np is None:
        raise RuntimeError("numpy is required for height computation")
    if values.size == 0:
        return None
    h = float(np.percentile(values, percentile))
    return float(max(min_height, min(max_height, h)))


def compute_base(values: np.ndarray) -> Optional[float]:
    """Compute a base elevation using the median of raster samples."""
    if np is None:
        raise RuntimeError("numpy is required for base height computation")
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

        base_values = sample_raster_values(dtm_path, geom)

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

        ndsm_values = sample_raster_values(ndsm_path, geom)
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
