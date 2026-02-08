import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from va_lidar_context.providers.vgin import _geometry_to_bbox, parse_laz_url


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
