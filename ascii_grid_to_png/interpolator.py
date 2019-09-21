from typing import Tuple, Any, Optional

from numpy.core.multiarray import ndarray
from scipy.interpolate import griddata
import numpy as np


class Interpolator:

    def __init__(
            self,
            points: ndarray,
            values: ndarray,
            bbox: Optional[Tuple[float, float, float, float]],
            interpolation_method: str,
            scale: float
    ):
        self.points = points
        self.values = values
        self.grid_data = None
        self.bbox = bbox
        self.method = interpolation_method
        self.scale = scale

    def compute(self) -> Tuple[Tuple[float, float, float, float], ndarray]:
        bbox = self._get_bbox()
        grid_x, grid_y = self._create_grid(bbox)
        return bbox, griddata(
            self.points,
            self.values,
            (grid_x, grid_y),
            method=self.method
        )

    def _get_bbox(self) -> Tuple[float, float, float, float]:
        if self.bbox is not None:
            return self.bbox
        else:
            min_x, min_y = np.amin(self.points, axis=0)
            max_x, max_y = np.amax(self.points, axis=0)
            return min_x, min_y, max_x, max_y

    def _create_grid(
            self,
            bbox: Tuple[float, float, float, float]
    ) -> Tuple[Any, Any]:
        min_x, min_y, max_x, max_y = bbox
        return np.mgrid[
               min_x:max_x:1./self.scale, min_y:max_y:1./self.scale
               ]
