from typing import List
import click

from ascii_grid_to_png import AsciiGridDataReader


@click.command()
@click.option('--range-min', default=0.0,
              help='The minimum value. Defaults to 0.')
@click.option('--range-max', default=255.0,
              help='The maximum value. Defaults to 255.')
@click.option('--bbox', default=None,
              help='The xllcorner,yllcorner,xurcorner,yurcorner bbox. Defaults to the full extents.')
@click.option('--scale', default=1,
              help='The size of the png being output. Defaults to 1.')
@click.argument('asc_files', nargs=-1)
@click.argument('output_file', nargs=1)
def cli(
        range_min: float,
        range_max: float,
        bbox: str,
        scale: float,
        asc_files: List[str],
        output_file: str
):
    """Output a PNG file from *.asc files"""

    ascii_grid_data_reader = AsciiGridDataReader()
    ascii_grids = []
    for asc_file in asc_files:
        ascii_grids.append(ascii_grid_data_reader.read(asc_file))


if __name__ == '__main__':
    cli()
