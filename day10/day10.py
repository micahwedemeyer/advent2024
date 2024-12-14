import unittest
from gameboard import Gameboard
from point import Point
from trail import Trail

def read_input(filename):
    with open(filename, 'r') as input:
        return input.readlines()

class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_lines = read_input("input2.txt")
        self.gameboard = Gameboard(self.raw_lines)

    def test_get_trailheads(self):
        trailheads = self.gameboard.get_trailheads()
        self.assertEqual(9, len(trailheads))
        t1 = trailheads[0]
        self.assertEqual(0, t1.value)
        self.assertEqual((0,2), t1.pt.loc())

        t9 = trailheads[8]
        self.assertEqual(0, t9.value)
        self.assertEqual((7,1), t9.pt.loc())

    def test_gameboard_iterable(self):
        pts = [pt for pt,val in self.gameboard]
        vals = [val for pt,val in self.gameboard]
        pt1 = pts[0]
        val1 = vals[0]
        self.assertEqual((0,0), pt1.loc())
        self.assertEqual(8, val1)

    def test_get_valid_steps(self):
        trailheads = self.gameboard.get_trailheads()
        t1 = trailheads[0]
        steps = t1.get_valid_steps()
        self.assertEqual((0,3), steps[0].loc())
        self.assertEqual((1,2), steps[1].loc())

        pt_8 = Point((4,4))
        t8 = Trail(self.gameboard[pt_8], pt_8, self.gameboard)
        self.assertEqual(8, t8.value)
        steps = t8.get_valid_steps()
        self.assertEqual(3, len(steps))
        self.assertEqual((3,4), steps[0].loc())
        self.assertEqual((4,5), steps[1].loc())
        self.assertEqual((5,4), steps[2].loc())

    # def test_get_complete_trails(self):
    #     trailheads = self.gameboard.get_trailheads()
    #     th1 = trailheads[0]
    #     trails = th1.get_complete_trails()
    #     self.assertEqual(5, len(th1.get_complete_trails()))

    def test_get_unique_destination_trails(self):
        trailheads = self.gameboard.get_trailheads()
        th1 = trailheads[0]
        trails = th1.get_unique_destination_trails()
        self.assertEqual(5, len(trails))

# unittest.main()

gameboard = Gameboard(read_input("input.txt"))
trailheads = gameboard.get_trailheads()
ratings = [len(trailhead.get_complete_trails()) for trailhead in trailheads]
# uniques = [unique for trailhead in trailheads for unique in trailhead.get_unique_destination_trails()]
print(sum(ratings))