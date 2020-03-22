class Bbox:

    xllcorner: float
    yllcorner: float
    xurcorner: float
    yurcorner: float

    @staticmethod
    def create_from_center_and_size(
        xcenter: float,
        ycenter: float,
        size: float
    ) -> 'Bbox':
        return Bbox(
            xcenter - size / 2,
            ycenter - size / 2,
            xcenter + size / 2,
            ycenter + size / 2
        )

    def __init__(
            self,
            xllcorner: float,
            yllcorner: float,
            xurcorner: float,
            yurcorner: float
    ):
        self.xllcorner = xllcorner
        self.yllcorner = yllcorner
        self.xurcorner = xurcorner
        self.yurcorner = yurcorner
