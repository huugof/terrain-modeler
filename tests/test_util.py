import unittest

from va_lidar_context.util import iter_offsets


class TestUtil(unittest.TestCase):
    def test_iter_offsets(self):
        self.assertEqual(list(iter_offsets(4500, 2000)), [0, 2000, 4000])
        self.assertEqual(list(iter_offsets(2000, 2000)), [0])


if __name__ == "__main__":
    unittest.main()
