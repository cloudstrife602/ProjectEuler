import inflect
p = inflect.engine()


def numToWords(num):
    return p.number_to_words(num)
    pass


def stringClean(string):
    trans = string.maketrans('', '', ' -')
    return string.translate(trans)


def numberLetterCount(num):
    return len(stringClean(numToWords(num)))

# number = 115
# print(numToWords(number))
# print(stringClean(numToWords(number)))
# print(numberLetterCount(number))

sum = 0
for i in range(1, 1001):
    sum += numberLetterCount(i)

print(sum)
