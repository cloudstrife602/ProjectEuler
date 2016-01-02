import unittest
from app.path import Path

class TestPE18(unittest.TestCase):

    def setUp(self):
        self.triangle = [
            [3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]
        ]
        self.p = Path()

    def test_requiredBits(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertEqual(p.requiredBits(), len(triangle))

    def test_init(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertEqual(p.triangle, triangle)
        self.assertEqual(p.path_length, len(triangle))

    def test_nodeMax(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertEqual(p.nodeMax(2, 0), 10)
        self.assertEqual(p.nodeMax(2, 1), 13)
        self.assertEqual(p.nodeMax(2, 2), 15)

    ''' Raises errors when i and j are out of bounds'''
    def test_nodeMax_error_when_i_and_j_out_of_bounds(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertRaises(IndexError, p.nodeMax, 5, 5)

    ''' Raises errors when i is out of bounds'''
    def test_nodeMax_error_when_i_is_out_of_bounds(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertRaises(IndexError, p.nodeMax, 5, 0)
        self.assertRaises(IndexError, p.nodeMax, -1, 0)

    ''' Raises errors when j is out of bounds'''
    def test_nodeMax_error_when_j_is_out_of_bounds(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertRaises(IndexError, p.nodeMax, 0, 1)
        self.assertRaises(IndexError, p.nodeMax, 0, -1)
        self.assertRaises(IndexError, p.nodeMax, 1, 2)
        self.assertRaises(IndexError, p.nodeMax, 1, -1)
        self.assertRaises(IndexError, p.nodeMax, 2, 3)
        self.assertRaises(IndexError, p.nodeMax, 2, -1)
        self.assertRaises(IndexError, p.nodeMax, 3, 4)
        self.assertRaises(IndexError, p.nodeMax, 3, -1)


    def test_max(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertEqual(p.max(), 23)

    def test_quickMax(self):
        triangle = self.triangle
        p = self.p
        p.init(triangle)
        self.assertEqual(p.quickMax(), 23)


if __name__ == '__main__':
    unittest.main()
