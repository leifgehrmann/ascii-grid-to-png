import unittest
import os

from ascii_grid_to_png import AsciiGridReader


class TestAsciiGridQuery(unittest.TestCase):

    def test_read(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        asc_file = test_dir + '/data/test.asc'
        reader = AsciiGridReader()
        grid_data = reader.read(asc_file)
