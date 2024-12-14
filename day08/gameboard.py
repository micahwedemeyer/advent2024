class Gameboard:
    def __init__(self, lines):
        self.matrix = self._parse_lines(lines)
        self.frequencies = self._parse_frequencies()

    def _parse_lines(self, lines):
        return [list(line.strip()) for line in lines]

    def _parse_frequencies(self):
        return set([ch for row in self.matrix for ch in row if ch != '.'])

    def in_bounds(self, loc):
        r, c = loc
        return r >= 0 and r < len(self.matrix) and c >= 0 and c < len(self.matrix[r])

    def find_antinodes(self, loc_a, loc_b):
        antis = [loc_a, loc_b]
        diff_a = (loc_a[0] - loc_b[0], loc_a[1] - loc_b[1])
        diff_b = (loc_b[0] - loc_a[0], loc_b[1] - loc_a[1])

        in_bounds = True
        loc = loc_a
        while in_bounds:
            loc = (loc[0] + diff_a[0], loc[1] + diff_a[1])
            in_bounds = self.in_bounds(loc)
            if in_bounds:
                antis.append(loc)

        in_bounds = True
        loc = loc_b
        while in_bounds:
            loc = (loc[0] + diff_b[0], loc[1] + diff_b[1])
            in_bounds = self.in_bounds(loc)
            if in_bounds:
                antis.append(loc)

        return antis

    def find_antennae(self, frequency):
        return [(r,c) for r in range(len(self.matrix)) for c in range(len(self.matrix[r])) if self.matrix[r][c] == frequency]

    def find_all_antinodes_by_freq(self, frequency):
        locs = self.find_antennae(frequency)
        loc_pairs = [(locs[i], locs[j]) for i in range(len(locs)) for j in range(i + 1,len(locs))]
        antinodes = [self.find_antinodes(pair[0], pair[1]) for pair in loc_pairs]
        return set([loc for pair in antinodes for loc in pair])

    def find_all_antinodes(self):
        return set([antinode for freq in self.frequencies for antinode in self.find_all_antinodes_by_freq(freq)])
