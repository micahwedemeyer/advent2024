class Trail:
    def __init__(self, value, pt, gameboard, parent = None):
        self.value = value
        self.pt = pt
        self.gameboard = gameboard
        self.parent = parent

    def get_valid_steps(self):
        steps = [self.pt.left(), self.pt.up(), self.pt.right(), self.pt.down()]
        return [step for step in steps if self.gameboard.is_in_bounds(step) and self.gameboard[step] == self.target_value()]

    def get_complete_trails(self):
        if self.value == 9:
            return [self]

        return [t for step in self.get_valid_steps() for t in Trail(self.target_value(), step, self.gameboard, self).get_complete_trails()]

    def get_unique_destination_trails(self):
        all_trails = self.get_complete_trails()
        destination_pts = set()
        destinations = []
        for t in all_trails:
            if t.pt not in destination_pts:
                destination_pts.add(t.pt)
                destinations.append(t) 

        return destinations

    def target_value(self):
        return self.value + 1

    def path(self):
        if self.parent is None:
            return [self.pt]
        else:
            return self.parent.path() + [self.pt]