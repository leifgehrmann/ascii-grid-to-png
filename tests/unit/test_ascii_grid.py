import unittest

from ascii_grid_to_png import AsciiGrid


class TestAsciiGrid(unittest.TestCase):

    def test_constructor_and_getters(self):
        input_grid_data = [
            [20, 40, 50],
            [50, 30, 20]
        ]

        grid_data = AsciiGrid(3, 2, 0, 0, 1, None, input_grid_data)

        assert grid_data.get_ncols() == 3
        assert grid_data.get_nrows() == 2
        assert grid_data.get_xllcorner() == 0
        assert grid_data.get_yllcorner() == 0
        assert grid_data.get_cellsize() == 1
        assert grid_data.get_nodata_value() is None
