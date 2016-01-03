import unittest
from app.pe21 import PE21


class TestPE21(unittest.TestCase):
    def setUp(self):
        self.c = PE21()

    def test_properDivisors(self):
        c = self.c
        self.assertEqual(c.properDivisors(1), [])
        self.assertEqual(c.properDivisors(4), [1, 2])
        self.assertEqual(c.properDivisors(220),
                         [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
        self.assertEqual(c.properDivisors(284),
                         [1, 2, 4, 71, 142])

    def test_d_n(self):
        c = self.c
        self.assertEqual(c.d(1), 0)
        self.assertEqual(c.d(220), 284)
        self.assertEqual(c.d(284), 220)

    def test_isAmicable(self):
        c = self.c
        self.assertEqual(c.isAmicable(1), 0)
        self.assertEqual(c.isAmicable(6), 0)
        self.assertEqual(c.isAmicable(220), 1)
        self.assertEqual(c.isAmicable(284), 1)

    def test_if_d_n_is_n_number_is_not_amicable(self):
        c = self.c
        self.assertEqual(c.d(6), c.d(c.d(6)))
        self.assertEqual(c.isAmicable(6), 0)


if __name__ == '__main__':
    unittest.main()
