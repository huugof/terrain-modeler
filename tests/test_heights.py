import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

try:
    import numpy as np
except Exception:  # pragma: no cover
    np = None

from va_lidar_context.heights import compute_height, fallback_height


@unittest.skipIf(np is None, "numpy not installed")
class TestHeights(unittest.TestCase):
    def test_compute_height_percentile_and_clamp(self):
        values = np.array([0, 10, 20, 30, 40], dtype=float)
        h = compute_height(values, percentile=90, min_height=8, max_height=25)
        self.assertAlmostEqual(h, 25.0)

    def test_compute_height_empty(self):
        values = np.array([], dtype=float)
        self.assertIsNone(
            compute_height(values, percentile=95, min_height=8, max_height=300)
        )

    def test_fallback_height_bldgheight(self):
        props = {"BLDGHEIGHT": 42}
        h = fallback_height(props, floor_to_floor=10)
        self.assertEqual(h, (42.0, "BLDGHEIGHT"))

    def test_fallback_height_numstories(self):
        props = {"NUMSTORIES": 3}
        h = fallback_height(props, floor_to_floor=12)
        self.assertEqual(h, (36.0, "NUMSTORIES"))

    def test_fallback_height_none(self):
        props = {"NUMSTORIES": None}
        h = fallback_height(props, floor_to_floor=10)
        self.assertIsNone(h)


if __name__ == "__main__":
    unittest.main()
