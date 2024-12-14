from guard import Guard

class Gameboard:
    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self.matrix[key[0]][key[1]]
        return self.matrix[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            self.matrix[key[0]][key[1]] = value
        else:
            self.matrix[key] = value

    
    def extract_guard(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == '^':
                    # Replace the guard with an empty space
                    self.matrix[r][c] = '.'
                    return Guard((r,c),'^')

    def is_in_bounds(self, loc):
        r,c = loc
        return r >= 0 and r < len(self.matrix) and c >= 0 and c < len(self.matrix[r])

    def clone(self):
        return Gameboard([row.copy() for row in self.matrix])

    def with_new_obstacle_at(self, loc):
        board = self.clone()
        board[loc] = '#'
        return board
