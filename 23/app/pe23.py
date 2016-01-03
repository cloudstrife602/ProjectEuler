"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""


class PE23(object):

    def properDivisors(self, n):
        if (n in (0, 1)):
            return []
        divisors = [1]
        for i in range(2, int(pow(n, 0.5)) + 1):
            if (n % i == 0):
                divisors.append(i)
                if not (int(n/i) == i):
                    divisors.append(int(n/i))
        return sorted(divisors)

    def abundantNumber(self, n):
        difference = sum(self.properDivisors(n)) - n
        if (difference > 0):
            return 1
        elif (difference == 0):
            return 0
        else:
            return -1


p = PE23()
limit = 28123
s = 0
abundantNumbers = set()
for n in range(1, limit + 1):
    # add number to list if it is abundant
    if (p.abundantNumber(n) > 0):
        abundantNumbers.add(n)
    # add number if it cannot be formed from the sum of 2 abundant numbers
    if not any((n - abn in abundantNumbers) for abn in abundantNumbers):
        s += n

# print(p.properDivisors(4))
# print(abundantNumbers)
print(s)
