import unittest
import os
from app.pe22 import PE22

class TestPE22(unittest.TestCase):
    def setUp(self):
        self.p = PE22()

    def test_importFromFile(self):
        p = self.p
        p.importFromFile('test/sample_names.txt')
        self.assertEqual(p.names,
                         ['JAMES', 'KYLE', 'NATALIE', 'EMILY', 'ISAAC'])

    def test_sorting(self):
        p = self.p
        p.importFromFile('test/sample_names.txt')
        p.sort()
        self.assertEqual(p.names,
                         ['EMILY', 'ISAAC', 'JAMES', 'KYLE', 'NATALIE'])

    def test_charValue(self):
        p = self.p
        self.assertEqual(p.charValue('A'), 1)
        self.assertEqual(p.charValue('B'), 2)
        self.assertEqual(p.charValue('C'), 3)
        self.assertEqual(p.charValue('D'), 4)
        self.assertEqual(p.charValue('E'), 5)
        self.assertEqual(p.charValue('F'), 6)
        self.assertEqual(p.charValue('G'), 7)
        self.assertEqual(p.charValue('H'), 8)
        self.assertEqual(p.charValue('I'), 9)
        self.assertEqual(p.charValue('J'), 10)
        self.assertEqual(p.charValue('K'), 11)
        self.assertEqual(p.charValue('L'), 12)
        self.assertEqual(p.charValue('M'), 13)
        self.assertEqual(p.charValue('N'), 14)
        self.assertEqual(p.charValue('O'), 15)
        self.assertEqual(p.charValue('P'), 16)
        self.assertEqual(p.charValue('Z'), 26)

    def test_wordValue(self):
        p = self.p
        self.assertEqual(p.wordValue('COLIN'), 53)

    def test_wordScore(self):
        p = self.p
        p.importFromFile('test/sample_names.txt')
        p.sort()
        self.assertEqual(p.wordScore(1, "EMILY"), 64)
        self.assertEqual(p.wordScore(2, "ISAAC"), 66)
        self.assertEqual(p.wordScore(3, "JAMES"), 144)
        self.assertEqual(p.wordScore(4, "KYLE"), 212)
        self.assertEqual(p.wordScore(5, "NATALIE"), 310)

    def test_score(self):
        p = self.p
        p.importFromFile('test/sample_names.txt')
        p.sort()
        self.assertEqual(p.score(), 64+66+144+212+310)

if __name__ == '__main__':
    unittest.main()
