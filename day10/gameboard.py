from trail import Trail
from gameboard_iterable import GameboardIterable

class Gameboard:
    def __init__(self, lines):
        self.matrix = self._parse_lines(lines)

    def _parse_lines(self, lines):
        return [self.__line_to_int_line(line) for line in lines]

    def __line_to_int_line(self, line):
        return [int(c) for c in list(line.strip())]

    def __getitem__(self, pt):
        return self.matrix[pt.r][pt.c]

    def __iter__(self):
        return GameboardIterable(self)

    def get_trailheads(self):
        return [Trail(val, pt, self) for pt, val in self if val == 0]

    def is_in_bounds(self, pt):
        return pt.is_in_bounds(self.matrix)
