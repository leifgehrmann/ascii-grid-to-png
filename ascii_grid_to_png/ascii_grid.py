from typing import List, Optional, Generator

from ascii_grid_to_png import AsciiGridHeader


class AsciiGrid(AsciiGridHeader):

    def __init__(
            self,
            ncols: int,
            nrows: int,
            xllcorner: float,
            yllcorner: float,
            cellsize: float,
            nodata_value: Optional[float],
            values: List[List[float]]
    ):
        super().__init__(
            ncols,
            nrows,
            xllcorner,
            yllcorner,
            cellsize,
            nodata_value
        )
        self.values = values

    def get_values(self) -> List[List[float]]:
        return self.values
