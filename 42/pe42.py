def charValue(char):
    base = ord('a') - 1
    return ord(char) - base


def wordValue(word):
    num = 0
    for char in word.lower():
        num += charValue(char)
    return num


def genTriangleNumbers(n):
    tNums = []
    for i in range(0, n+1):
        tNums.append(int((i*(i+1))/2))
    return tNums


def testWordValue():
    if (wordValue("SKY") == 55):
        pass


triangleNumbers = genTriangleNumbers(25)

words = []
f = open("p042_words.txt", "r")
line = f.readline().replace('"', '')

words = line.split(',')

count = 0
for word in words:
    try:
        index = triangleNumbers.index(wordValue(word))
    except Exception as e:
        continue
    if (index):
        print(word+": "+str(wordValue(word)))
        count += 1

print(count)
