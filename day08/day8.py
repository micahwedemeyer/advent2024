import unittest
from gameboard import Gameboard

def read_input(filename):
    with open(filename, 'r') as input:
        return input.readlines()


class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_lines = read_input("input2.txt")
        self.board = Gameboard(self.raw_lines)
        self.lines2 = read_input("input3.txt")
        self.board2 = Gameboard(self.lines2)

    def test_parse_board(self):
        self.assertEqual(set(['0', 'A']), self.board.frequencies)

    def test_in_bounds(self):
        self.assertTrue(self.board.in_bounds((0,0)))
        self.assertTrue(self.board.in_bounds((1,1)))
        self.assertTrue(self.board.in_bounds((3,2)))
        self.assertTrue(self.board.in_bounds((11,11)))

        self.assertFalse(self.board.in_bounds((1,-1)))
        self.assertFalse(self.board.in_bounds((-1,1)))
        self.assertFalse(self.board.in_bounds((11,12)))
        self.assertFalse(self.board.in_bounds((12,11)))

    # def test_find_antinodes(self):
    #     antis = self.board.find_antinodes((1,2), (3,1))
    #     self.assertEqual((-1, 3), antis[0])
    #     self.assertEqual((5, 0), antis[1])

    def test_find_antennae(self):
        ants = self.board.find_antennae('A')
        self.assertEqual(3, len(ants))
        self.assertEqual((5,6), ants[0])

        ants = self.board.find_antennae('0')
        self.assertEqual(4, len(ants))
        self.assertEqual((1,8), ants[0])

    # def test_find_all_antinodes_by_freq(self):
    #     ants_a = self.board.find_all_antinodes_by_freq('A')
    #     ants_0 = self.board.find_all_antinodes_by_freq('0')
    #     ant_set = set(ants_a)
    #     ant_set.update(ants_0)
    #     self.assertEqual(14, len(ant_set))

    # def test_find_all_antinodes(self):
    #     ants = self.board.find_all_antinodes()
    #     self.assertEqual(14, len(ants))
    
    ### Part 2
    def test_find_antinodes(self):
        antis = self.board2.find_antinodes((0, 0), (2, 1))
        # Both nodes...
        self.assertIn((0, 0), antis)
        self.assertIn((2, 1), antis)

        # And the ones in line
        self.assertIn((4, 2), antis)
        self.assertIn((6, 3), antis)
        self.assertIn((8, 4), antis)


    def test_find_all_antinodes_by_freq(self):
        # (0,5), (2.6) ... (8,4), and some T's... (0,0), (2,1)
        antis = self.board2.find_all_antinodes_by_freq('T')
        self.assertEqual(9, len(antis))
        self.assertIn((0, 5), antis)
        self.assertIn((2, 6), antis)
        self.assertIn((8, 4), antis)
        self.assertIn((0, 0), antis)
        self.assertIn((2, 1), antis)

    def test_find_all_antinodes(self):
        antis = self.board.find_all_antinodes()
        self.assertEqual(34, len(antis))

# unittest.main()

lines = read_input("input.txt")
board = Gameboard(lines)
ants = board.find_all_antinodes()
print(len(ants))
