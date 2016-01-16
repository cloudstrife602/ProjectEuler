import unittest
from app.pe24 import PE24


class TestPE24(unittest.TestCase):
    """ Defines tests for Project Euler 24"""

    def setUp(self):
        self.p = PE24()

    def test_permutations(self):
        p = self.p
        permutations = []
        self.assertEqual(p.permutations([0, 1, 2]),
                         [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0),
                          (2, 0, 1), (2, 1, 0)])


if __name__ == '__main__':
    unittest.main()
