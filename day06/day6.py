from gameboard import Gameboard
import unittest

def read_input(filename):
    with open(filename, 'r') as input:
        return input.readlines()

def build_matrix(raw_lines):
    return [list(line.strip()) for line in raw_lines]


class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_lines = read_input("input2.txt")
        self.mat = build_matrix(self.raw_lines)
        self.board = Gameboard(self.mat)

    def test_build_gameboard(self):
        self.assertEqual(self.board[0][0], '.')
        self.assertEqual(self.board[0][4], '#')
        self.assertEqual(self.board[3][2], '#')

    def test_extract_guard(self):
        self.assertEqual(self.board[6][4], '^')
        guard = self.board.extract_guard()
        self.assertEqual(guard.loc(), (6,4))
        self.assertEqual(self.board[6][4], '.')

    def test_is_in_bounds(self):
        self.assertTrue(self.board.is_in_bounds((1,1)))
        self.assertTrue(self.board.is_in_bounds((2,3)))
        self.assertFalse(self.board.is_in_bounds((-1,3)))
        self.assertFalse(self.board.is_in_bounds((1,44)))
        self.assertTrue(self.board.is_in_bounds((3,0)))

    def test_step_up(self):
        guard = self.board.extract_guard()
        guard.facing = '^'

        self.assertEqual(guard.loc(), (6,4))
        self.assertEqual(guard.path, [(6,4,'^')])
        guard.step(self.board)
        self.assertEqual(guard.loc(), (5, 4))
        self.assertEqual(guard.path, [(6,4,'^'),(5,4,'^')])
        self.assertTrue(guard.is_on_board)

        # Jump to top, step off board
        guard.r, guard.c = (0,3)
        guard.step(self.board)
        self.assertFalse(guard.is_on_board)
        # Nothing added to path?
        self.assertEqual(guard.path, [(6,4,'^'),(5,4,'^')])

        
    def test_step_blocker_rotates(self):
        guard = self.board.extract_guard()
        self.assertEqual(guard.loc(), (6,4))
        self.assertEqual(guard.path, [(6,4,'^')])
        self.assertEqual(guard.facing, '^')

        # Jump below a blocker
        guard.r, guard.c = (4,2)
        guard.step(self.board)

        # Just rotate. No path change, no location change
        self.assertEqual(guard.loc(), (4,2))
        self.assertEqual(guard.path, [(6,4,'^')])
        self.assertEqual(guard.facing, '>')


    #### Eh, doesn't work anymore because I calculate loops as we go now via hashtable

    # def test_is_looping(self):
    #     guard = self.board.extract_guard()

    #     # All different positions
    #     guard.path = [(3,0,'^'), (2,0,'^'), (1,0,'^')]
    #     guard.speed_path = zip([((r,c,f), 1) for r,c,f in guard.path])
    #     self.assertFalse(guard.is_looping)

    #     # Same position, different facing
    #     guard.path = [(3,0,'^'), (2,0,'^'), (2,0,'>')]
    #     guard.speed_path = zip([((r,c,f), 1) for r,c,f in guard.path])
    #     self.assertFalse(guard.is_looping)

    #     # Same position, same facing...loop!
    #     guard.path = [(3,0,'^'), (2,0,'^'), (2,0,'^')]
    #     guard.speed_path = zip([((r,c,f), 1) for r,c,f in guard.path])
    #     self.assertTrue(guard.is_looping)

    def test_with_new_obstacle_at(self):
        self.assertEqual(self.board[0][0], '.')
        self.assertEqual(self.board[0][4], '#')
        self.assertEqual(self.board[3][2], '#')

        board2 = self.board.with_new_obstacle_at((0,0))

        self.assertEqual(board2[0][0], '#')
        self.assertEqual(board2[0][1], '.')
        self.assertEqual(board2[0][4], '#')

        # Original unchanged?
        self.assertEqual(self.board[0][0], '.')






# unittest.main()

raw_lines = read_input("input.txt")
mat = build_matrix(raw_lines)
board = Gameboard(mat)
orig_guard = board.extract_guard()
guard_start = orig_guard.loc()
print(f"guard start: {guard_start}")

board = Gameboard(build_matrix(raw_lines))

loop_count = 0
for r in range(len(mat)):
    for c in range(len(mat[r])):
        print(f"({r},{c})")
        # Can't step on guard...
        if (r,c) != guard_start:
            new_board = board.with_new_obstacle_at((r,c))
            new_guard = new_board.extract_guard()

            while new_guard.is_on_board and not new_guard.is_looping:
                new_guard.step(new_board)

            if new_guard.is_looping:
                loop_count += 1

print(loop_count)


# print(guard.loc())
# while guard.is_on_board:
#     guard.step(board)

# steps = len(guard.path)
# deduped = len(set(guard.path))

# print(steps)
# print(deduped)
