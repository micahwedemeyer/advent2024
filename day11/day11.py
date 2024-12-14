import unittest
from stone import Stone

def read_input(filename):
    with open(filename, 'r') as input:
        return input.read().strip()


class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.raw = read_input("input2.txt")
        self.generation = 5
        self.library = {}

    def test_is_even_digits(self):
        s1 = Stone(999, self.generation, self.library)
        s2 = Stone(1111, self.generation, self.library)
        s3 = Stone(22, self.generation, self.library)
        s4 = Stone(98765, self.generation, self.library)

        self.assertTrue(s2._is_even_digits())
        self.assertTrue(s3._is_even_digits())

        self.assertFalse(s1._is_even_digits())
        self.assertFalse(s4._is_even_digits())

    def test_halfsies(self):
        s1 = Stone(4567, self.generation, self.library)
        s2 = Stone(987654, self.generation, self.library)
        s3 = Stone(60609065, self.generation, self.library)
        s4 = Stone(7009, self.generation, self.library)

        self.assertEqual([45, 67], [s.val for s in s1._halfsies()])
        self.assertEqual([987, 654], [s.val for s in s2._halfsies()])
        self.assertEqual([6060, 9065], [s.val for s in s3._halfsies()])
        self.assertEqual([70, 9], [s.val for s in s4._halfsies()])

    def test_blink(self):
        s0 = Stone(0, self.generation, self.library)
        s1 = Stone(1, self.generation, self.library)
        s2 = Stone(60609065, self.generation, self.library)
        s3 = Stone(3, self.generation, self.library)
        s4 = Stone(125, self.generation, self.library)
        s5 = Stone(17, self.generation, self.library)
        s6 = Stone(253000, self.generation, self.library)

        self.assertEqual([1], [s.val for s in s0.blink()])
        self.assertEqual([2024], [s.val for s in s1.blink()])
        self.assertEqual([6060, 9065], [s.val for s in s2.blink()])
        self.assertEqual([2024 * 3], [s.val for s in s3.blink()])
        self.assertEqual([253000], [s.val for s in s4.blink()])
        self.assertEqual([1, 7], [s.val for s in s5.blink()])
        self.assertEqual([253, 0], [s.val for s in s6.blink()])

    def test_score(self):
        library = {}
        s0 = Stone(125, 6, library)
        s1 = Stone(17, 6, library)
        self.assertEqual(22, s0.score() + s1.score())

        s2 = Stone(125, 25, library)
        s3 = Stone(17, 25, library)
        self.assertEqual(55312, s2.score() + s3.score())

    def test_score_2(self):
        stone_vals = [0, 1, 10, 99, 999]
        library = {}
        stones = [Stone(val, 1, library) for val in stone_vals]
        self.assertEqual(7, sum([stone.score() for stone in stones]))



# unittest.main()

generations = 75
library = {}
stones = [Stone(int(val), generations, library) for val in read_input("input.txt").split()]
print([stone.val for stone in stones])
scores = [stone.score() for stone in stones]
print(scores)
print(sum(scores))

# subs = stones
# for gen in range(0, generations):
#     print(f"gen {gen}")
#     subs = [st for stone in subs for st in stone.blink()]
#     print([s.val for s in subs])