class Point:
    def __init__(self, loc):
        self.r, self.c = loc

    def loc(self):
        return (self.r, self.c)

    def is_in_bounds(self, matrix):
        return self.r >= 0 and self.r < len(matrix) and self.c >= 0 and self.c < len(matrix[self.r])

    def __add__(self, loc):
        return Point((self.r + loc[0], self.c + loc[1]))

    def __eq__(self, pt):
        return self.r == pt.r and self.c == pt.c

    def __hash__(self):
        return self.r * self.c

    def left(self):
        return self + (0, -1)
    
    def right(self):
        return self + (0, 1)

    def up(self):
        return self + (-1, 0)
    
    def down(self):
        return self + (1, 0)