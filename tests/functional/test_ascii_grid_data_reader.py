import unittest
import os

from ascii_grid_to_png import AsciiGridDataReader


class TestAsciiGridDataReader(unittest.TestCase):

    def test_constructor_and_defaults(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        asc_file = test_dir + '/test.asc'
        reader = AsciiGridDataReader()
        grid_data = reader.read(asc_file)

        assert grid_data.get_ncols() == 5
        assert grid_data.get_nrows() == 4
        assert grid_data.get_xllcorner() == 200
        assert grid_data.get_yllcorner() == -200
        assert grid_data.get_cellsize() == 2
        assert grid_data.get_nodata_value() == -9999
