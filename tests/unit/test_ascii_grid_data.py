import unittest

from ascii_grid_to_png import AsciiGridData


class TestAsciiGridData(unittest.TestCase):

    def test_constructor_and_defaults(self):
        input_grid_data = [
            [20, 40, 50],
            [50, 30, 20]
        ]

        grid_data = AsciiGridData(input_grid_data)

        assert grid_data.get_ncols() == 3
        assert grid_data.get_nrows() == 2
        assert grid_data.get_xllcorner() == 0
        assert grid_data.get_yllcorner() == 0
        assert grid_data.get_cellsize() == 1
        assert grid_data.get_nodata_value() is None

    def test_setters(self):
        input_grid_data = [
            [20, 40, 50],
            [50, 30, 20]
        ]

        grid_data = AsciiGridData(input_grid_data)

        grid_data.set_xllcorner(123)
        grid_data.set_yllcorner(456)
        grid_data.set_cellsize(20)
        grid_data.set_nodata_value(-9999)

        assert grid_data.get_xllcorner() == 123
        assert grid_data.get_yllcorner() == 456
        assert grid_data.get_cellsize() == 20
        assert grid_data.get_nodata_value() == -9999
