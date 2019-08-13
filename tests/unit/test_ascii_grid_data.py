import unittest
from typing import Generator

from ascii_grid_to_png import AsciiGridData


class TestAsciiGridData(unittest.TestCase):

    def test_constructor_and_defaults(self):
        input_grid_data = [
            [20, 40, 50],
            [50, 30, 20]
        ]

        grid_data = AsciiGridData(
            input_grid_data,
            123,
            456,
            20,
            -9999
        )

        assert grid_data.get_ncols() == 3
        assert grid_data.get_nrows() == 2
        assert grid_data.get_xllcorner() == 123
        assert grid_data.get_yllcorner() == 456
        assert grid_data.get_cellsize() == 20
        assert grid_data.get_nodata_value() == -9999

    def test_nodata_value_defaults_to_none(self):
        input_grid_data = [
            [20, 40, 50],
            [50, 30, 20]
        ]

        grid_data = AsciiGridData(input_grid_data, 0, 0, 1)

        assert grid_data.get_nodata_value() is None

    def test_get_total_data_points(self):
        input_grid_data = [
            [20, -999, -999],
            [-999, 30, 20]
        ]

        data = AsciiGridData(input_grid_data, 0, 0, 1)

        assert data.get_total_data_points() == 6
        assert data.get_total_data_points(False) == 6

        data_with_nodata_values = AsciiGridData(input_grid_data, 0, 0, 1, -999)

        assert data_with_nodata_values.get_total_data_points() == 6
        assert data_with_nodata_values.get_total_data_points(False) == 3

    def test_get_data_points(self):
        grid_data = [
            [20, -999, -999],
            [-999, 30, 20]
        ]

        data_with_nodata_values = AsciiGridData(grid_data, 100, 20, 5, -999)
        data_points = data_with_nodata_values.get_data_points()

        assert isinstance(data_points, Generator)
        data_points = list(data_points)
        assert data_points == [
            (100, 20, 20),
            (105, 20, -999),
            (110, 20, -999),
            (100, 25, -999),
            (105, 25, 30),
            (110, 25, 20)
        ]

        data_points = data_with_nodata_values.get_data_points(False)
        assert isinstance(data_points, Generator)
        data_points = list(data_points)
        assert data_points == [
            (100, 20, 20),
            (105, 25, 30),
            (110, 25, 20)
        ]
