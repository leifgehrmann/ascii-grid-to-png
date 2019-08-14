import unittest
import os

from ascii_grid_to_png import AsciiGridDataReader


class TestAsciiGridDataReader(unittest.TestCase):

    @staticmethod
    def _get_file(filename):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        return '%s/%s' % (test_dir, filename)

    def test_constructor_and_defaults(self):
        reader = AsciiGridDataReader()
        grid_data = reader.read(self._get_file('data_default.asc'))

        assert grid_data.get_ncols() == 5
        assert grid_data.get_nrows() == 4
        assert grid_data.get_xllcorner() == 200
        assert grid_data.get_yllcorner() == -200
        assert grid_data.get_cellsize() == 2
        assert grid_data.get_nodata_value() == -9999

    def test_invalid_headers(self):
        reader = AsciiGridDataReader()
        with self.assertRaises(Exception) as context:
            reader.read(self._get_file('data_invalid_headers_1.asc'))
        print(str(context.exception))
        self.assertTrue(
            'could not convert string to float: \'four\''
            in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            reader.read(self._get_file('data_invalid_headers_2.asc'))
        print(str(context.exception))
        self.assertTrue(
            'Invalid header: Total points is equal to ncols * nrows'
            in str(context.exception)
        )

        with self.assertRaises(Exception) as context:
            reader.read(self._get_file('data_invalid_headers_3.asc'))
        print(str(context.exception))
        self.assertTrue(
            'Invalid header: 124 ncols'
            in str(context.exception)
        )

    def test_missing_headers(self):
        reader = AsciiGridDataReader()
        with self.assertRaises(Exception) as context:
            reader.read(self._get_file('data_missing_headers.asc'))
        self.assertTrue(
            'Unexpected missing headers: ncols/nrows'
            in str(context.exception)
        )

    def test_unexpected_ncols(self):
        reader = AsciiGridDataReader()
        with self.assertRaises(Exception) as context:
            reader.read(self._get_file('data_unexpected_ncols.asc'))
        self.assertTrue(
            'Unexpected column count: Expected 3, got 5'
            in str(context.exception)
        )

    def test_unexpected_nrows(self):
        reader = AsciiGridDataReader()
        with self.assertRaises(Exception) as context:
            reader.read(self._get_file('data_unexpected_nrows.asc'))
        self.assertTrue(
            'Unexpected row count: Expected 10, got 4'
            in str(context.exception)
        )
