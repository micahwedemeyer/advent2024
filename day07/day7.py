import unittest
from equation import Equation

def read_input(filename):
    with open(filename, 'r') as input:
        return input.readlines()


class Tester(unittest.TestCase):
    def test_parse_equation(self):
        line = "21037: 9 7 18 13"
        e = Equation(line)
        self.assertEqual(21037, e.target)
        self.assertEqual([9, 7, 18, 13], e.components)

    def test_build_optree(self):
        line = "21037: 9 7 18 13"
        e = Equation(line)
        tree = e.build_op_tree()
        self.assertEqual(13, tree.value)
        self.assertEqual(18, tree.subtree.value)
        self.assertEqual(7, tree.subtree.subtree.value)
        self.assertEqual(9, tree.subtree.subtree.subtree.value)
        self.assertIsNone(tree.subtree.subtree.subtree.subtree)

    def test_calc_vals(self):
        line = "21037: 9 7 18 13"
        e = Equation(line)
        tree = e.build_op_tree()
        vals = tree.walk_tree()
        self.assertNotIn(21037, vals)

        line2 = "3267: 81 40 27"
        e2 = Equation(line2)
        tree2 = e2.build_op_tree()
        vals2 = tree2.walk_tree()
        self.assertIn(3267, vals2)

        line3 = "156: 15 6"
        e3 = Equation(line3)
        tree3 = e3.build_op_tree()
        vals3 = tree3.walk_tree()
        self.assertIn(156, vals3)

    def test_is_satisfied(self):
        line = "21037: 9 7 18 13"
        e = Equation(line)
        self.assertFalse(e.is_satisfied())

        line2 = "3267: 81 40 27"
        e2 = Equation(line2)
        self.assertTrue(e2.is_satisfied())

        line3 = "7290: 6 8 6 15"
        e3 = Equation(line3)
        self.assertTrue(e3.is_satisfied())


# unittest.main()

lines = read_input("input.txt")
equations = [Equation(line) for line in lines]
sats = [eq for eq in equations if eq.is_satisfied()]
sat_targets = [eq.target for eq in sats]
print(len(sats))
print(sum(sat_targets))
