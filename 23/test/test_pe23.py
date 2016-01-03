import unittest
from app.pe23 import PE23

class TestPE23(unittest.TestCase):
    def setUp(self):
        self.p = PE23()

    def test_properDivisors(self):
        p = self.p
        self.assertEqual(p.properDivisors(1), [])
        self.assertEqual(p.properDivisors(4), [1, 2])
        self.assertEqual(p.properDivisors(220),
                         [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
        self.assertEqual(p.properDivisors(284),
                         [1, 2, 4, 71, 142])

    def test_abundantNumber_number_is_perfect(self):
        p = self.p
        self.assertEqual(p.abundantNumber(28), 0)

    def test_abundantNumber_number_is_abundant(self):
        p = self.p
        self.assertEqual(p.abundantNumber(12), 1)

    def test_abundantNumber_number_is_deficient(self):
        p = self.p
        self.assertEqual(p.abundantNumber(2), -1)


if __name__ == '__main__':
    unittest.main()
