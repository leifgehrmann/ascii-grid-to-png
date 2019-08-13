from typing import List

import numpy as np
from numpy.core.multiarray import ndarray

from ascii_grid_to_png import AsciiGridData


class AsciiGridDataNdarray:

    def __init__(self, ascii_grids: List[AsciiGridData]):
        self.ascii_grids = ascii_grids
        self.total_points = None

    def generate(self) -> ndarray:

        pass

    def _create_empty_points_shape(self):
        return np.empty(shape=[self.get_number_of_points(), 2])

    def _create_empty_values_shape(self):
        return np.empty(self.get_number_of_points())

    def _fill_shapes_with_ascii_grids(
            self,
            points: ndarray,
            values: ndarray,
            ascii_grid: AsciiGridData,
            offset: int
    ):
        

    def _fill_shapes_with_ascii_grid(
            self,
            points: ndarray,
            values: ndarray,
            ascii_grid: AsciiGridData,
            offset: int
    ):
        idx = offset
        for x, y, z in ascii_grid.get_data_points():
            points[idx][0] = x
            points[idx][1] = y
            values[idx] = z
            idx += 1

    def get_number_of_points(self) -> int:
        if self.total_points is not None:
            return self.total_points

        total_points = 0
        for ascii_grid in self.ascii_grids:
            total_points += ascii_grid.get_total_data_points(False)

        self.total_points = total_points
        return self.total_points

        # my_array = np.empty(predict_length())
# for i, el in enumerate(gimme()): my_array[i] = el
