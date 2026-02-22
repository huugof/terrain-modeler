import unittest
from pathlib import Path

from va_lidar_context.util import is_path_within, iter_offsets


class TestUtil(unittest.TestCase):
    def test_iter_offsets(self):
        self.assertEqual(list(iter_offsets(4500, 2000)), [0, 2000, 4000])
        self.assertEqual(list(iter_offsets(2000, 2000)), [0])

    def test_is_path_within_true(self, tmp_path=None):
        import tempfile

        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            child = base / "subdir" / "file.txt"
            self.assertTrue(is_path_within(base, child))

    def test_is_path_within_false(self, tmp_path=None):
        import tempfile

        with tempfile.TemporaryDirectory() as d1:
            with tempfile.TemporaryDirectory() as d2:
                base = Path(d1)
                other = Path(d2) / "file.txt"
                self.assertFalse(is_path_within(base, other))

    def test_is_path_within_rejects_traversal(self, tmp_path=None):
        import tempfile

        with tempfile.TemporaryDirectory() as d:
            base = Path(d) / "safe"
            traversal = Path(d) / "safe" / ".." / "escape"
            # After resolve, ".." escapes the safe dir — should return False
            self.assertFalse(is_path_within(base, traversal))


if __name__ == "__main__":
    unittest.main()
