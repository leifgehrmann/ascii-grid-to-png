import unittest
import os

from ascii_grid_to_png import AsciiGridReader


class TestAsciiGridReader(unittest.TestCase):

    def test_read(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        asc_file = test_dir + '/data/test.asc'
        reader = AsciiGridReader()
        grid_data = reader.read(asc_file)

        assert grid_data.get_ncols() == 5
        assert grid_data.get_nrows() == 4
        assert grid_data.get_xllcorner() == 200
        assert grid_data.get_yllcorner() == -200
        assert grid_data.get_cellsize() == 2
        assert grid_data.get_nodata_value() == -9999
        assert grid_data.get_values() == [
            [-9999, -9999, 0, 0.2, 0.3],
            [1.5, 2.3, 0, -9999, 4.2],
            [4.5, 6.3, 4, 10, 4.5],
            [9.2, 20.1, 15.2, 18.1, 12.2]
        ]

    def test_read_header(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        asc_file = test_dir + '/data/test.asc'
        reader = AsciiGridReader()
        grid_data_header = reader.read(asc_file)

        assert grid_data_header.get_ncols() == 5
        assert grid_data_header.get_nrows() == 4
        assert grid_data_header.get_xllcorner() == 200
        assert grid_data_header.get_yllcorner() == -200
        assert grid_data_header.get_cellsize() == 2
        assert grid_data_header.get_nodata_value() == -9999

    def test_read_invalid_header_splits_exception(self):
        with self.assertRaises(Exception) as err:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            asc_file = test_dir + '/data/test_invalid_header_splits.asc'
            AsciiGridReader().read(asc_file)
        self.assertEqual(
            'Invalid header: ncols 5 2',
            str(err.exception)
        )

    def test_read_invalid_header_missing_exception(self):
        with self.assertRaises(Exception) as err:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            asc_file = test_dir + '/data/test_invalid_header_missing.asc'
            AsciiGridReader().read(asc_file)
        print(err.exception)
        self.assertEqual(
            'Unexpected missing headers: ncols/nrows',
            str(err.exception)
        )

    def test_read_invalid_header_type_exception(self):
        with self.assertRaises(Exception) as err:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            asc_file = test_dir + '/data/test_invalid_header_type.asc'
            AsciiGridReader().read(asc_file)
        print(err.exception)
        self.assertEqual(
            'ncols/nrows must be an int',
            str(err.exception)
        )

    def test_read_invalid_cols_exception(self):
        with self.assertRaises(Exception) as err:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            asc_file = test_dir + '/data/test_invalid_cols.asc'
            AsciiGridReader().read(asc_file)
        print(err.exception)
        self.assertEqual(
            'Unexpected column count: Expected 5, got 4',
            str(err.exception)
        )

    def test_read_invalid_rows_exception(self):
        with self.assertRaises(Exception) as err:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            asc_file = test_dir + '/data/test_invalid_rows.asc'
            AsciiGridReader().read(asc_file)
        print(err.exception)
        self.assertEqual(
            'Unexpected row count: Expected 4, got 3',
            str(err.exception)
        )
