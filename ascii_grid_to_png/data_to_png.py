from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from numpy.core.multiarray import ndarray


class DataToPng:
    def __init__(
            self,
            bbox: Tuple[float, float, float, float],
            grid_z: ndarray,
            filename: str
    ):
        self.bbox = bbox
        self.grid_z = grid_z
        self.filename = filename

    def output(self):
        sizes = np.shape(self.grid_z)
        width = float(sizes[0])
        height = float(sizes[1])

        fig = plt.figure()
        fig.set_size_inches(width/height, 1, forward=False)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)

        ax.imshow(self.grid_z.T, origin='upper')
        plt.savefig(self.filename, dpi=height)
        plt.close()
