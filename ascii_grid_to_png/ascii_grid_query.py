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

        return []

    def get_points_in_bbox(
            self,
            bbox: Bbox
    ) -> List[Tuple[Tuple[float, float], float]]:
        return []
