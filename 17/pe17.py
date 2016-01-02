import inflect
import unittest


class TestPE17Methods(unittest.TestCase):

    def test_numToWords(self):
        number = 342
        self.assertEqual(numToWords(number), "three hundred and forty-two")
        number = 115
        self.assertEqual(numToWords(number), "one hundred and fifteen")

    def test_stringClean(self):
        self.assertEqual(stringClean("three hundred and forty-two"), "threehundredandfortytwo")
        self.assertEqual(stringClean("one hundred and fifteen"), "onehundredandfifteen")

    def test_numberLetterCount(self):
        self.assertEqual(numberLetterCount(342), 23)
        self.assertEqual(numberLetterCount(115), 20)
        
p = inflect.engine()


def numToWords(num):
    return p.number_to_words(num)
    pass


def stringClean(string):
    trans = string.maketrans('', '', ' -')
    return string.translate(trans)


def numberLetterCount(num):
    return len(stringClean(numToWords(num)))


sum = 0
for i in range(1, 1001):
    sum += numberLetterCount(i)

print(sum)
