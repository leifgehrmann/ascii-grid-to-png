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
            grid_data: List[List[float]]
    ):
        super().__init__(
            ncols,
            nrows,
            xllcorner,
            yllcorner,
            cellsize,
            nodata_value
        )
        self.grid_data = grid_data
        self.total_data_points = None

    def get_total_data_points(self, include_nodata: bool = True) -> int:
        if include_nodata or self.nodata_value is None:
            return self.get_nrows() * self.get_ncols()

        total_data_points = 0
        for row in self.grid_data:
            for col in row:
                if col != self.nodata_value:
                    total_data_points += 1
        return total_data_points

    def get_data_points(
            self,
            include_nodata: bool = True
    ) -> Generator[float, None, None]:
        for y_idx, row in enumerate(self.grid_data):
            y = self.yllcorner + (y_idx + 0.5) * self.cellsize
            for x_idx, col in enumerate(row):
                if not include_nodata and col == self.nodata_value:
                    continue
                x = self.xllcorner + (x_idx + 0.5) * self.cellsize
                yield x, y, col
