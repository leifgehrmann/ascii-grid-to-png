import unittest

import numpy as np

from ascii_grid_to_png import Interpolator


class TestInterpolator(unittest.TestCase):

    def test_compute_returns_correct_grid_size(self):
        scale = 0.5
        bbox = (10, 10, 30, 40)
        min_x, min_y, max_x, max_y = bbox

        output_bbox, grid_z = Interpolator(
            np.array([
                [12, 12],
                [12, 22],
                [12, 32],
                [22, 12],
                [22, 32],
            ]),
            np.array([
                4,
                10,
                30,
                3,
                5
            ]),
            bbox,
            'linear',
            0.5
        ).compute()

        expected_size = (max_x - min_x) * scale * (max_y - min_y) * scale

        assert bbox == output_bbox
        assert grid_z.size == expected_size

    def test_compute_with_none_bbox_returns_max_extents(self):
        scale = 0.5
        bbox = (12, 12, 22, 32)
        min_x, min_y, max_x, max_y = bbox

        output_bbox, grid_z = Interpolator(
            np.array([
                [12, 12],
                [12, 22],
                [12, 32],
                [22, 12],
                [22, 32],
            ]),
            np.array([
                4,
                10,
                30,
                3,
                5
            ]),
            None,
            'linear',
            0.5
        ).compute()

        expected_size = (max_x - min_x) * scale * (max_y - min_y) * scale

        assert bbox == output_bbox
        assert grid_z.size == expected_size
