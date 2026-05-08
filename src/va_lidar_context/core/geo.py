from __future__ import annotations

import math
from typing import Any, Dict, List, Mapping, Tuple

from pyproj import CRS, Transformer
from shapely.geometry import shape
from shapely.ops import transform

BBoxWGS84 = Tuple[float, float, float, float]

FEET_PER_METER = 3.28084


def bbox_contains(
    outer: Mapping[str, float] | BBoxWGS84,
    inner: BBoxWGS84,
) -> bool:
    """Return True if the inner bbox is fully contained by the outer bbox."""
    if isinstance(outer, tuple):
        outer_bbox = {
            "xmin": outer[0],
            "ymin": outer[1],
            "xmax": outer[2],
            "ymax": outer[3],
        }
    else:
        outer_bbox = outer
    xmin, ymin, xmax, ymax = inner
    return (
        outer_bbox["xmin"] <= xmin <= outer_bbox["xmax"]
        and outer_bbox["xmin"] <= xmax <= outer_bbox["xmax"]
        and outer_bbox["ymin"] <= ymin <= outer_bbox["ymax"]
        and outer_bbox["ymin"] <= ymax <= outer_bbox["ymax"]
    )


def bbox_from_center_wgs84(
    lat: float,
    lon: float,
    size: float,
    units: str,
) -> BBoxWGS84:
    """Compute a WGS84 bbox centered at (lat, lon) with a square size."""
    if units == "feet":
        size_m = size / FEET_PER_METER
    else:
        size_m = size
    half = size_m / 2.0
    # Use a local azimuthal equidistant projection so that meter offsets
    # represent true ground distances regardless of latitude (unlike Web
    # Mercator which distorts ~27% at lat 38°).
    aeqd = CRS.from_proj4(f"+proj=aeqd +lat_0={lat} +lon_0={lon} +datum=WGS84 +units=m")
    to_aeqd = Transformer.from_crs("EPSG:4326", aeqd, always_xy=True)
    to_wgs = Transformer.from_crs(aeqd, "EPSG:4326", always_xy=True)
    cx, cy = to_aeqd.transform(lon, lat)
    corners = [
        to_wgs.transform(cx - half, cy - half),
        to_wgs.transform(cx - half, cy + half),
        to_wgs.transform(cx + half, cy - half),
        to_wgs.transform(cx + half, cy + half),
    ]
    xs = [c[0] for c in corners]
    ys = [c[1] for c in corners]
    return (min(xs), min(ys), max(xs), max(ys))


def get_unit_scale(crs: CRS, output_units: str, latitude: float | None = None) -> float:
    """Return a multiplier to convert CRS units to desired output units.

    When *latitude* is provided and the CRS is Web Mercator (EPSG:3857),
    the scale is corrected for Mercator distortion so that output
    coordinates represent true ground distances.
    """
    axis = crs.axis_info[0] if crs.axis_info else None
    to_meters = axis.unit_conversion_factor if axis and axis.unit_conversion_factor else 1.0
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
