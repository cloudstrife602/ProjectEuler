""" Project Euler Prompt:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?"""
import math


class PE25(object):
    """Define methods for Project Euler 25."""
    PHI = 1.61803399

    def numberOfDigits(self, number):
        """Return the number of digits in number."""
        return round(math.log10(number) + 1)

    def fibonacci(self, n):
        if n in [1, 2]:
            return 1
        else:
            fibs = [1, 0, 1]
            i = 1
            while i <= n:
                fibs[i % 3] = fibs[(i+1) % 3] + fibs[(i + 2) % 3]
                i += 1
            return fibs[i % 3]

    def firstFibWithNDigits(self, n):
        if n < 1:
            raise(ValueError)
        if n == 1:
            return 1
        numerator = math.log(10)*(n-1) + math.log(5)/2
        denominator = math.log(self.PHI)
        intermediate = numerator / denominator
        return math.ceil(intermediate)

p = PE25()
n = 1
f = p.firstFibWithNDigits(n)
print("The first fibonacci number with", n, "digits is", f)
print("Fib(", f, "): ", p.fibonacci(f))
