from typing import List, Tuple

from ascii_grid_to_png import AsciiGrid, Bbox


class AsciiGridQuery:

    ascii_grid: AsciiGrid

    def __init__(self, ascii_grid: AsciiGrid):
        self.ascii_grid = ascii_grid

    def get_points_in_range(
            self,
            center: Tuple[float, float],
            size: float
    ) -> List[Tuple[Tuple[float, float], float]]:
        return self.get_points_in_bbox(Bbox.create_from_center_and_size(
            center[0],
            center[1],
            size
        ))

    def get_points_in_bbox(
            self,
            bbox: Bbox
    ) -> List[Tuple[Tuple[float, float], float]]:
        x_min_index = max(0.0, self._get_x_index(bbox.xllcorner))

        y_min_index = self._get_y_index(bbox.yllcorner)
        x_max_index = self._get_x_index(bbox.xurcorner)
        y_max_index = self._get_y_index(bbox.yurcorner)
        return []

    def _get_x_index(self, x: float) -> float:
        return (x - self.ascii_grid.xllcorner) / self.ascii_grid.cellsize - 0.5

    def _get_y_index(self, y: float) -> float:
        return (y - self.ascii_grid.yllcorner) / self.ascii_grid.cellsize - 0.5
