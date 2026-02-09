from __future__ import annotations

from va_lidar_context.core.geo import bbox_contains, bbox_from_center_wgs84


def test_bbox_from_center_contains_center():
    bbox = bbox_from_center_wgs84(37.0, -78.0, 1000.0, "feet")
    assert bbox[0] < -78.0 < bbox[2]
    assert bbox[1] < 37.0 < bbox[3]


def test_bbox_from_center_accurate_size():
    """Verify the bbox produces true ground distances, not Mercator-distorted ones."""
    from pyproj import CRS, Transformer

    size_ft = 5000.0
    lat, lon = 38.0, -78.0
    bbox = bbox_from_center_wgs84(lat, lon, size_ft, "feet")

    # Measure the actual ground distance of the bbox using an equidistant projection
    aeqd = CRS.from_proj4(f"+proj=aeqd +lat_0={lat} +lon_0={lon} +datum=WGS84 +units=m")
    to_aeqd = Transformer.from_crs("EPSG:4326", aeqd, always_xy=True)
    x_min, y_min = to_aeqd.transform(bbox[0], bbox[1])
    x_max, y_max = to_aeqd.transform(bbox[2], bbox[3])
    width_m = x_max - x_min
    height_m = y_max - y_min
    size_m = size_ft / 3.28084

    # Should be within 0.1% of requested size
    assert abs(width_m - size_m) / size_m < 0.001
    assert abs(height_m - size_m) / size_m < 0.001


def test_bbox_contains_tuple_and_dict():
    outer = (-10.0, -10.0, 10.0, 10.0)
    inner = (-5.0, -5.0, 5.0, 5.0)
    assert bbox_contains(outer, inner)
    assert bbox_contains(
        {"xmin": -10.0, "ymin": -10.0, "xmax": 10.0, "ymax": 10.0},
        inner,
    )
