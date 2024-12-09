import unittest

class Tester(unittest.TestCase):
    def test_something(self):
        val1 = 44
        val2 = 66
        self.assertEqual(110, val1 + val2)

    def test_something_else(self):
        l = [2,4,6,8]
        self.assertIn(4, l)
        self.assertNotIn(5,l)
        self.assertEqual(4, len(l))



unittest.main()