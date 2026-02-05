import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from va_lidar_context.vgin_tile import (
    _geometry_to_bbox,
    normalize_coordinates,
    parse_laz_url,
)


class TestNormalizeCoordinates(unittest.TestCase):
    def test_lat_lon_order(self):
        # Google Maps style: lat, lon (37.538, -77.436)
        lon, lat = normalize_coordinates(37.538, -77.436)
        self.assertEqual(lon, -77.436)
        self.assertEqual(lat, 37.538)

    def test_lon_lat_order(self):
        # GeoJSON style: lon, lat (-77.436, 37.538)
        lon, lat = normalize_coordinates(-77.436, 37.538)
        self.assertEqual(lon, -77.436)
        self.assertEqual(lat, 37.538)

    def test_invalid_coordinates(self):
        # Both outside valid latitude range
        with self.assertRaises(ValueError):
            normalize_coordinates(-100, -150)

    def test_both_positive_assumes_lat_lon(self):
        # Both positive and valid as lat - assume lat, lon (Google style)
        lon, lat = normalize_coordinates(37.5, 38.5)
        self.assertEqual(lat, 37.5)
        self.assertEqual(lon, 38.5)


class TestVginTile(unittest.TestCase):
    def test_parse_laz_url(self):
        html = '<a href="https://example.com/data.laz">Download</a>'
        self.assertEqual(parse_laz_url(html), "https://example.com/data.laz")

    def test_parse_laz_url_missing(self):
        self.assertIsNone(parse_laz_url(""))
        self.assertIsNone(parse_laz_url("no href here"))

    def test_geometry_to_bbox_rings(self):
        geom = {"rings": [[[0, 1], [2, 3], [4, 5], [0, 1]]]}
        self.assertEqual(_geometry_to_bbox(geom), (0, 1, 4, 5))

    def test_geometry_to_bbox_paths(self):
        geom = {"paths": [[[10, 20], [30, 40]]]}
        self.assertEqual(_geometry_to_bbox(geom), (10, 20, 30, 40))


if __name__ == "__main__":
    unittest.main()
