from __future__ import annotations

from typing import Mapping, Tuple

from pyproj import CRS, Transformer

from .heights import FEET_PER_METER

BBoxWGS84 = Tuple[float, float, float, float]


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
