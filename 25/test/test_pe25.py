import unittest
from app.pe25 import PE25


class TestPEDummy(unittest.TestCase):
    def setUp(self):
        self.p = PE25()

    def test_numberOfDigits(self):
        p = self.p
        self.assertEqual(p.numberOfDigits(1), 1)
        self.assertEqual(p.numberOfDigits(10), 2)
        self.assertEqual(p.numberOfDigits(100), 3)
        self.assertEqual(p.numberOfDigits(10**999), 1000)

    def test_fibonacci_start(self):
        p = self.p
        self.assertEqual(p.fibonacci(1), 1)
        self.assertEqual(p.fibonacci(2), 1)

    def test_fibonacci_intermediate(self):
        p = self.p
        self.assertEqual(p.fibonacci(3), 2)
        self.assertEqual(p.fibonacci(10), 55)
        self.assertEqual(p.fibonacci(100), 354224848179261915075)

    def test_firstFibWithNDigits(self):
        p = self.p
        self.assertEqual(p.firstFibWithNDigits(1), 1)
        self.assertEqual(p.firstFibWithNDigits(2), 7)
        self.assertEqual(p.firstFibWithNDigits(3), 12)
        self.assertEqual(p.firstFibWithNDigits(4), 17)
        self.assertEqual(p.firstFibWithNDigits(1000), 4782)

    def test_firstFibWithNDigits_raises_ValueError(self):
        p = self.p
        self.assertRaises(ValueError, p.firstFibWithNDigits, 0)

if __name__ == '__main__':
    unittest.main()
