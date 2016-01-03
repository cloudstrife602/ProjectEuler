"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

class PE21(object):

    def properDivisors(self, n):
        if (n in (0, 1)):
            return []
        divisors = [1]
        for i in range(2, int(pow(n, 0.5)) + 1):
            if (n % i == 0):
                divisors.append(i)
                divisors.append(int(n/i))
        return sorted(divisors)

    def d(self, n):
        return sum(self.properDivisors(n))

    def isAmicable(self, n):
        d_result = self.d(n)
        if (n != d_result and n == self.d(d_result)):
            return 1
        else:
            return 0

p = PE21()
target = 10000
amicable_numbers = []
for i in range(1, target):
    if (p.isAmicable(i)):
        amicable_numbers.append(i)

print(amicable_numbers)
print(sum(amicable_numbers))
