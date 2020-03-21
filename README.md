# ascii-grid-to-png

Work in progress.

A simple script that reads multiple [ASCII raster] files and renders a
basic PNG image. Requires python3.

```
$ ascii-grid-to-png --help
Usage: ascii-grid-to-png [OPTIONS] [ASC_FILES]... OUTPUT_FILE

  Output a PNG file from *.asc files

Options:
  --range-min FLOAT  The minimum value. Defaults to 0.
  --range-max FLOAT  The maximum value. Defaults to 255.
  --bbox TEXT        The xllcorner,yllcorner,xurcorner,yurcorner bbox.
                     Defaults to the full extents.
  --scale INTEGER    The size of the png being output. Defaults to 1.
  --help             Show this message and exit.
```

## Installing and running

This project uses [poetry], so assuming you have it installed, you can just clone
this repository then run:

```
$ poetry install
$ poetry run ascii-grid-to-png --help
```

Otherwise, a regular install using pip should work.

```
$ pip install -r requirements.txt
$ python setup.py install
$ ascii-grid-to-png --help
```

[ASCII raster data]: http://webhelp.esri.com/arcgisdesktop/9.3/index.cfm?TopicName=ESRI%20ASCII%20Raster%20format
[poetry]: https://python-poetry.org
