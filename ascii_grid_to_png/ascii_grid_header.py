from typing import Optional


class AsciiGridHeader:

    def __init__(
            self,
            ncols: int,
            nrows: int,
            xllcorner: float,
            yllcorner: float,
            cellsize: float,
            nodata_value: Optional[float]
    ):
        self.ncols = ncols
        self.nrows = nrows
        self.xllcorner = xllcorner
        self.yllcorner = yllcorner
        self.cellsize = cellsize
        self.nodata_value = nodata_value
        self.total_data_points = None

    def get_ncols(self) -> int:
        return self.ncols

    def get_nrows(self) -> int:
        return self.nrows

    def get_xllcorner(self) -> float:
        return self.xllcorner

    def get_yllcorner(self) -> float:
        return self.yllcorner

    def get_cellsize(self) -> float:
        return self.cellsize

    def get_nodata_value(self) -> Optional[float]:
        return self.nodata_value
