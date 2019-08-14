import unittest

import numpy as np

from ascii_grid_to_png import AsciiGridData, AsciiGridDataNdarray


class TestAsciiGridData(unittest.TestCase):

    def test_generate_with_no_grids(self):
        grid_data_combined = AsciiGridDataNdarray([])
        assert grid_data_combined.get_number_of_points() == 0
        points, values = grid_data_combined.generate()
        assert points.size == 0
        assert values.size == 0

    def test_generate(self):
        grid_data_1 = AsciiGridData([
            [1, 3, 2],
            [1, 4, 4],
            [3, 4, 2],
            [0, 8, 2]
        ],
            10,
            20,
            5,
            4
        )

        grid_data_2 = AsciiGridData([
            [5, 5, 5],
            [5, 5, 5],
            [5, 4, 2],
            [5, 5, 5]
        ],
            110,
            120,
            5,
            4
        )

        grids = [grid_data_1, grid_data_2]
        grid_data_combined = AsciiGridDataNdarray(grids, False)
        assert grid_data_combined.get_number_of_points() == 20

        points, values = grid_data_combined.generate()
        assert points.size == 40
        assert values.size == 20

        assert np.array_equal(points[19], np.array([120, 135]))
