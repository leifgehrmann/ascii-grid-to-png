from typing import List, Tuple, Optional
import click

from ascii_grid_to_png import AsciiGridDataReader, \
    AsciiGridDataNdarray, \
    Interpolator, \
    DataToPng


@click.command()
@click.option('--range-min', default=0.0,
              help='The minimum value. Defaults to 0.')
@click.option('--range-max', default=255.0,
              help='The maximum value. Defaults to 255.')
@click.option('--bbox', default=None,
              help='The xllcorner,yllcorner,xurcorner,yurcorner bbox. '
                   'Defaults to the full extents. '
                   'E.g. 0,0,10,20 for a 10x20 box with the origin at 0, 0.')
@click.option('--interpolation-method', default='nearest',
              help='The interpolation method. '
                   'Either: linear, nearest, or cubic.')
@click.option('--scale', default=1.,
              help='The size of the png being output. '
                   'Defaults to 1. '
                   'E.g. 2 means output image will be 2 times as big, and '
                   '0.5 means the image will half as big.')
@click.argument('asc_files', nargs=-1)
@click.argument('output_file', nargs=1)
def cli(
        range_min: float,
        range_max: float,
        bbox: str,
        interpolation_method: str,
        scale: float,
        asc_files: List[str],
        output_file: str
):
    """Output a PNG file from *.asc files"""

    bbox_float = parse_bbox(bbox)

    ascii_grid_data_reader = AsciiGridDataReader()
    ascii_grids = []
    for asc_file in asc_files:
        print('reading: %s' % asc_file)
        ascii_grids.append(ascii_grid_data_reader.read(asc_file))

    print('joining data')
    points, values = AsciiGridDataNdarray(ascii_grids, False).generate()

    print('interpolating')
    output_bbox, grid_z = Interpolator(
        points,
        values,
        bbox_float,
        interpolation_method,
        scale
    ).compute()

    print('outputing')
    DataToPng(output_bbox, grid_z, output_file).output()


def parse_bbox(bbox) -> Optional[Tuple[float, float, float, float]]:
    if bbox is None:
        return None
    bbox_str = bbox.split(',')
    bbox_float = tuple([float(i) for i in bbox_str])[0:4]
    if len(bbox_float) != 4:
        raise Exception(
            'Invalid bbox: expected 4 numbers, not %d' % len(bbox_float)
        )
    return bbox_float


if __name__ == '__main__':
    cli()
