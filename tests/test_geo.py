from __future__ import annotations

from va_lidar_context.core.geo import bbox_contains, bbox_from_center_wgs84


def test_bbox_from_center_contains_center():
    bbox = bbox_from_center_wgs84(37.0, -78.0, 1000.0, "feet")
    assert bbox[0] < -78.0 < bbox[2]
    assert bbox[1] < 37.0 < bbox[3]


def test_bbox_contains_tuple_and_dict():
    outer = (-10.0, -10.0, 10.0, 10.0)
    inner = (-5.0, -5.0, 5.0, 5.0)
    assert bbox_contains(outer, inner)
    assert bbox_contains(
        {"xmin": -10.0, "ymin": -10.0, "xmax": 10.0, "ymax": 10.0},
        inner,
    )
