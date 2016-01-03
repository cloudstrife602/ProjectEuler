"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import os


class PE22(object):
    names = []

    def importFromFile(self, filename):
        path = os.path.abspath('.') + "/"
        with open(path + filename) as f:
            for line in f:
                line = line.replace('"', '')
                line = line.replace('\n', '')
                self.names = line.split(',')

    def sort(self):
        self.names.sort()

    def charValue(self, char):
        base = ord('A') - 1
        return ord(char) - base

    def wordValue(self, word):
        num = 0
        for char in word.upper():
            num += self.charValue(char)
        return num

    def wordScore(self, order, word):
        return order * self.wordValue(word)

    def score(self):
        names = self.names
        total = 0
        for i in range(0, len(names)):
            total += self.wordScore(i + 1, names[i])
        return total

p = PE22()
p.importFromFile('app/p022_names.txt')
p.sort()
print(p.score())
