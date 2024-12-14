class Guard:
    def __init__(self, loc, facing):
        self.r, self.c = loc
        self.facing = facing
        self.is_on_board = True
        self.path = [(self.r, self.c, self.facing)]
        self.speed_path = {(self.r, self.c, self.facing): 1}
        self.is_looping = False

    def loc(self):
        return (self.r, self.c)

    def step(self, gameboard):
        new_loc = None
        if self.facing == '^':
            new_loc = (self.r - 1, self.c)
        elif self.facing == '>':
            new_loc = (self.r, self.c + 1)
        elif self.facing == 'V':
            new_loc = (self.r + 1, self.c)
        elif self.facing == '<':
            new_loc = (self.r, self.c - 1)

        if not gameboard.is_in_bounds(new_loc):
            self.is_on_board = False
            return

        if gameboard[new_loc] == '#':
            self.rotate()
            return

        self.r, self.c = new_loc

        path_tuple = (self.r, self.c, self.facing)

        self.path.append(path_tuple)
        self.is_looping = path_tuple in self.speed_path
        self.speed_path[path_tuple] = 1

    def rotate(self):
        if self.facing == '^':
            self.facing = '>'
        elif self.facing == '>':
            self.facing = 'V'
        elif self.facing == 'V':
            self.facing = '<'
        elif self.facing == '<':
            self.facing = '^'
