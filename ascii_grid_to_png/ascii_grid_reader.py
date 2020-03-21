import re
from typing import Tuple, List, Union

from ascii_grid_to_png import AsciiGrid, AsciiGridHeader


class AsciiGridReader:
    valid_headers = [
        'ncols',
        'nrows',
        'xllcorner',
        'yllcorner',
        'cellsize',
        'nodata_value'
    ]

    def read(self, filepath: str) -> AsciiGrid:
        return self._read(filepath, False)

    def read_header(self, filepath: str) -> AsciiGridHeader:
        return self._read(filepath, True)

    def _read(
            self,
            filepath: str,
            header_only: bool
    ) -> Union[AsciiGrid, AsciiGridHeader]:
        headers_read = False
        headers_size_read = False
        headers_size_is_ints = False
        header_data = {}
        grid_data = []
        with open(filepath) as file:
            for line in file:

                # Read headers
                if not headers_read or \
                   not headers_size_read or \
                   not headers_size_is_ints or\
                   self._is_header(line):
                    if not self._is_header(line):
                        continue

                    header_param, header_value = self._read_header(line)
                    header_data[header_param] = header_value
                    headers_read = True
                    headers_size_read = 'ncols' in header_data and \
                                        'nrows' in header_data
                    if headers_size_read:
                        headers_size_is_ints = \
                            header_data['ncols'].is_integer() \
                            and header_data['nrows'].is_integer()
                    continue

                if header_only:
                    continue

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

        if not headers_size_read:
            raise Exception('Unexpected missing headers: ncols/nrows')

        if not headers_size_is_ints:
            raise Exception('ncols/nrows must be an int')

        if header_only:
            return AsciiGridHeader(
                int(header_data['ncols']),
                int(header_data['nrows']),
                header_data['xllcorner'],
                header_data['yllcorner'],
                header_data['cellsize'],
                header_data['nodata_value'] if 'nodata_value' in header_data else
                None
            )

        if len(grid_data) != header_data['nrows']:
            raise Exception(
                'Unexpected row count: Expected %d, got %d' % (
                    int(header_data['nrows']),
                    len(grid_data)
                )
            )

        return AsciiGrid(
            int(header_data['ncols']),
            int(header_data['nrows']),
            header_data['xllcorner'],
            header_data['yllcorner'],
            header_data['cellsize'],
            header_data['nodata_value'] if 'nodata_value' in header_data else
            None,
            grid_data
        )

    def _is_header(self, line) -> bool:
        for valid_header in self.valid_headers:
            if line.lower().startswith(valid_header + ' '):
                return True
        return False

    def _read_header(self, line: str) -> Tuple[str, float]:
        line = re.sub("[ \t]+", ' ', line).strip()
        line_split = line.split()
        if len(line_split) != 2:
            raise Exception('Invalid header: %s' % line)

        return line_split[0].lower(), float(line_split[1])

    @staticmethod
    def _read_grid_data_row(line: str) -> List[float]:
        row_strings = line.strip().split(' ')
        row = []
        for row_string in row_strings:
            row.append(float(row_string))
        return row
