from point import Point

class GameboardIterable:
    def __init__(self, gameboard):
        self.r = 0
        self.c = 0
        self.gameboard = gameboard

    def __next__(self):
        pt = Point((self.r, self.c))
        if self.gameboard.is_in_bounds(pt):
            # Value is tuple of (point, value)
            val = (pt, self.gameboard[pt])
            if self.c < len(self.gameboard.matrix[self.r]) - 1:
                self.c += 1
            else:
                self.c = 0
                self.r += 1
            return val
        else:
            raise StopIteration