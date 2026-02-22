import unittest
from unittest.mock import patch

try:
    import numpy as np
except Exception:  # pragma: no cover
    np = None

try:
    from shapely.geometry import Polygon
except Exception:  # pragma: no cover
    Polygon = None

from va_lidar_context.core.heights import (
    FootprintHeight,
    _ground_estimate,
    compute_height,
    derive_heights_from_point_cloud,
    fallback_height,
    heights_to_geojson,
)


@unittest.skipIf(np is None, "numpy not installed")
class TestHeights(unittest.TestCase):
    def test_compute_height_percentile_and_clamp(self):
        values = np.array([0, 10, 20, 30, 40], dtype=float)
        h = compute_height(values, percentile=90, min_height=8, max_height=25)
        self.assertAlmostEqual(h, 25.0)

    def test_compute_height_empty(self):
        values = np.array([], dtype=float)
        self.assertIsNone(compute_height(values, percentile=95, min_height=8, max_height=300))

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

    def test_ground_estimate_prefers_class2_median(self):
        ring_z = np.array([100.0, 100.2, 99.8, 100.1, 105.0], dtype=float)
        ring_cls = np.array([2, 2, 2, 2, 5], dtype=int)
        out = _ground_estimate(
            ring_z,
            ring_cls,
            dtm_path="unused",
            ring_geom=None,
            min_ground_pts=4,
        )
        self.assertEqual(out["method"], "class2_median")
        self.assertEqual(out["n_ground_pts"], 4)
        self.assertAlmostEqual(out["ground"], 100.05, places=2)

    @unittest.skipIf(Polygon is None, "shapely not installed")
    def test_heights_to_geojson_fields(self):
        geom = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
        rows = [
            FootprintHeight(
                geometry=geom,
                height=10.0,
                source="POINT_ROOF_P95",
                base_z=100.0,
                building_id="b1",
                qc={
                    "n_roof_pts": 20,
                    "n_ground_pts": 14,
                    "ground_method": "class2_median",
                    "roof_p95": 110.0,
                    "roof_p99": 111.0,
                    "ground_median": 100.0,
                    "flags": ["low_ground_pts"],
                },
            )
        ]
        data = heights_to_geojson(rows, z_to_meters=1.0)
        feat = data["features"][0]
        self.assertEqual(feat["properties"]["building_id"], "b1")
        self.assertAlmostEqual(feat["properties"]["height_m"], 10.0)
        self.assertAlmostEqual(feat["properties"]["height_ft"], 32.8084)
        self.assertEqual(feat["properties"]["n_roof_pts"], 20)
        self.assertEqual(feat["properties"]["ground_method"], "class2_median")
        self.assertEqual(feat["properties"]["qc_flags"], "low_ground_pts")

    @unittest.skipIf(Polygon is None, "shapely not installed")
    def test_point_cloud_height_not_clamped_by_min_max(self):
        geom = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
        features = [{"geometry": geom, "properties": {"building_id": "b1"}}]

        roof_pts = np.array(
            [
                [2, 2],
                [2, 4],
                [2, 6],
                [2, 8],
                [4, 2],
                [4, 4],
                [4, 6],
                [4, 8],
                [6, 2],
                [6, 4],
                [6, 6],
                [6, 8],
                [8, 2],
                [8, 4],
                [8, 6],
                [8, 8],
                [3, 3],
                [3, 7],
                [7, 3],
                [7, 7],
            ],
            dtype=float,
        )
        ground_pts = np.array(
            [
                [-2, 5],
                [12, 5],
                [5, -2],
                [5, 12],
                [-3, 2],
                [13, 2],
                [-3, 8],
                [13, 8],
                [2, -3],
                [8, -3],
                [2, 13],
                [8, 13],
                [-4, 5],
                [14, 5],
                [5, -4],
                [5, 14],
                [-2, 2],
                [12, 2],
                [-2, 8],
                [12, 8],
            ],
            dtype=float,
        )
        x = np.concatenate([roof_pts[:, 0], ground_pts[:, 0]])
        y = np.concatenate([roof_pts[:, 1], ground_pts[:, 1]])
        z = np.concatenate(
            [
                np.full((roof_pts.shape[0],), 120.0),
                np.full((ground_pts.shape[0],), 100.0),
            ]
        )
        cls = np.concatenate(
            [
                np.full((roof_pts.shape[0],), 6, dtype=int),
                np.full((ground_pts.shape[0],), 2, dtype=int),
            ]
        )

        with patch(
            "va_lidar_context.core.heights._extract_laz_points",
            return_value=(x, y, z, cls),
        ):
            heights, warnings = derive_heights_from_point_cloud(
                laz_path="unused.laz",
                dtm_path="unused.tif",
                features=features,
                percentile=95,
                min_height=30.0,
                max_height=40.0,
                floor_to_floor=10.0,
                z_to_meters=1.0,
                ndsm_path=None,
            )

        self.assertEqual(warnings, [])
        self.assertEqual(len(heights), 1)
        self.assertEqual(heights[0].source, "POINT_ROOF_P95")
        self.assertAlmostEqual(heights[0].base_z, 100.0)
        # If min/max clamping applied here, this would be 30.0, not 20.0.
        self.assertAlmostEqual(heights[0].height, 20.0)


if __name__ == "__main__":
    unittest.main()
