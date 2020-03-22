import unittest

from ascii_grid_to_png import Bbox


class TestBbox(unittest.TestCase):

    def test_constructor(self):
        bbox = Bbox(0, 1, 2, 3)
        assert bbox.xllcorner == 0
        assert bbox.yllcorner == 1
        assert bbox.xurcorner == 2
        assert bbox.yurcorner == 3

    def test_create_from_center_and_size(self):
        bbox = Bbox.create_from_center_and_size(2, 3, 2)
        assert bbox.xllcorner == 1
        assert bbox.yllcorner == 2
        assert bbox.xurcorner == 3
        assert bbox.yurcorner == 4
