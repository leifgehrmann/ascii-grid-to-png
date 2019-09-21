from typing import List, Optional, Generator


class AsciiGridData:

    def __init__(
            self,
            grid_data: List[List[float]],
            xllcorner: float,
            yllcorner: float,
            cellsize: float,
            nodata_value: Optional[float] = None
    ):
        self.grid_data = grid_data
        self.xllcorner = xllcorner
        self.yllcorner = yllcorner
        self.cellsize = cellsize
        self.nodata_value = nodata_value
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

    def get_ncols(self) -> int:
        return len(self.grid_data[0])

    def get_nrows(self) -> int:
        return len(self.grid_data)

    def get_xllcorner(self) -> float:
        return self.xllcorner

    def get_yllcorner(self) -> float:
        return self.yllcorner

    def get_cellsize(self) -> float:
        return self.cellsize

    def get_nodata_value(self) -> Optional[float]:
        return self.nodata_value
