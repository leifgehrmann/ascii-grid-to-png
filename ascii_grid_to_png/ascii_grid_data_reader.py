import re
from typing import Tuple, List

from ascii_grid_to_png import AsciiGridData


class AsciiGridDataReader:
    valid_headers = [
        'ncols',
        'nrows',
        'xllcorner',
        'yllcorner',
        'cellsize',
        'nodata_value'
    ]

    def read(self, filepath: str) -> AsciiGridData:
        headers_read = False
        header_data = {}
        grid_data = []
        with open(filepath) as file:
            for line in file:

                # Read headers
                if not headers_read and self._is_header(line):
                    if self._is_header(line):
                        header_param, header_value = self._read_header(line)
                        header_data[header_param] = header_value
                        continue
                    headers_read = True

                # Validate headers
                if 'ncols' not in header_data or 'nrows' not in header_data:
                    raise Exception('Unexpected missing headers: ncols/nrows')

                # Read grid data
                grid_data_row = self._read_grid_data_row(line)

                # Validate column count
                if int(header_data['ncols'] != len(grid_data_row)):
                    raise Exception(
                        'Unexpected column count: Expected %d, got %d' % (
                            int(header_data['ncols']),
                            len(grid_data_row)
                        )
                    )

                grid_data.append(self._read_grid_data_row(line))

        if len(grid_data) != header_data['nrows']:
            raise Exception(
                'Unexpected row count: Expected %d, got %d' % (
                    int(header_data['nrows']),
                    len(grid_data)
                )
            )

        grid_data = AsciiGridData(
            grid_data,
            header_data['xllcorner'],
            header_data['yllcorner'],
            header_data['cellsize'],
            header_data['nodata_value'] if 'nodata_value' in header_data else
            None
        )

        return grid_data

    def _is_header(self, line) -> bool:
        for valid_header in self.valid_headers:
            if valid_header in line.lower():
                return True
        return False

    def _read_header(self, line: str) -> Tuple[str, float]:
        line = re.sub("[ \t]+", ' ', line).strip()
        line_split = line.split()
        if len(line_split) != 2:
            raise Exception('Invalid header: %s' % line_split)

        if not self._is_header(line_split[0]):
            raise Exception('Invalid header: %s' % line_split)

        return line_split[0].lower(), float(line_split[1])

    @staticmethod
    def _read_grid_data_row(line: str) -> List[float]:
        row_strings = line.split(' ')
        row = []
        for row_string in row_strings:
            row.append(float(row_string))
        return row
