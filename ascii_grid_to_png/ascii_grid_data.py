from typing import List, Optional


class AsciiGridData:

    def __init__(self, grid_data: List[List[float]]):
        self.grid_data = grid_data
        self.xllcorner = 0
        self.yllcorner = 0
        self.cellsize = 1
        self.nodata_value = None

    def get_ncols(self) -> int:
        return len(self.grid_data[0])

    def get_nrows(self) -> int:
        return len(self.grid_data)

    def set_xllcorner(self, xllcorner: float) -> None:
        self.xllcorner = xllcorner

    def get_xllcorner(self) -> float:
        return self.xllcorner

    def set_yllcorner(self, yllcorner: float) -> None:
        self.yllcorner = yllcorner

    def get_yllcorner(self) -> float:
        return self.yllcorner

    def set_cellsize(self, cellsize: float) -> None:
        self.cellsize = cellsize

    def get_cellsize(self) -> float:
        return self.cellsize

    def set_nodata_value(self, nodata_value: float) -> None:
        self.nodata_value = nodata_value

    def get_nodata_value(self) -> Optional[float]:
        return self.nodata_value
