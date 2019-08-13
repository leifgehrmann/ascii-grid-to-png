from typing import List

from numpy.core.multiarray import ndarray
from scipy.interpolate import griddata
import numpy as np

from ascii_grid_to_png import AsciiGridData


class GridDataInterpolator:

    ascii_grids: List[AsciiGridData]

    def __init__(self):
        self.ascii_grids = []
        self.points = None
        self.values = None
        self.grid_data = []
        self.method = 'nearest'

    def add_ascii_grid_data(self, ascii_grid_data: AsciiGridData):
        self.ascii_grids.append(ascii_grid_data)

    def set_interpolation_method(self, method: str) -> None:
        self.method = method

    def compute(self) -> ndarray:
        self.points = self._create_points_shape()
        self.values = self._create_values_shape()

        self.get_data_points(False)

        grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
        return griddata(
            self.points,
            self.values,
            (grid_x, grid_y),
            method=self.method
        )

    def _fill_shape(self, shape: ndarray, ):

    def _create_points_shape(self) -> ndarray:
        return np.empty(shape=[self._get_number_of_points(), 2])

    def _create_values_shape(self) -> ndarray:
        return np.empty(shape=[self._get_number_of_points(), 1])

    def _get_number_of_points(self) -> int:
        total_points = 0
        for ascii_grid in self.ascii_grids:
            total_points += ascii_grid.get_total_data_points(False)
        return total_points
