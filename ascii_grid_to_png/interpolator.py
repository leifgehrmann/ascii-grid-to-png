from typing import List, Tuple

from numpy.core.multiarray import ndarray
from scipy.interpolate import griddata
import numpy as np


class Interpolator:

    def __init__(
            self,
            points: ndarray,
            values: ndarray,
            bbox: Tuple[float, float, float, float],
            scale: float
    ):
        self.points = points
        self.values = values
        self.grid_data = None
        self.method = 'nearest'

    def set_interpolation_method(self, method: str) -> None:
        self.method = method

    def compute(self) -> ndarray:
        grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
        return griddata(
            self.points,
            self.values,
            (grid_x, grid_y),
            method=self.method
        )
