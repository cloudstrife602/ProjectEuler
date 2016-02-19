"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?"""


class PE7(object):
    """Defines needed methods for Project Euler 7."""

    def IsPrime(self, n):
        """Test n for primality."""
        if (n < 1):
            raise ValueError("Number must be a positive integer.")
        if (n == 1):
            # 1 is never prime.
            return False
        if (n in (2, 3)):
            return True
        if (n % 2 == 0):
            return False
        if (n % 3 == 0):
            return False
        k = 1
        while (k * 6 - 1 <= n ** 0.5):
            if (n % (k * 6 - 1) == 0):
                return False
            if (n % (k * 6 + 1) == 0):
                return False
            k += 1
        return True

    def NthPrime(self, n):
        if (n == 1):
            return 2
        if (n == 2):
            return 3
        count = 2
        k = 1
        while (count < n):
            index = k * 6
            nminus = index - 1
            nplus = index + 1
            if (self.IsPrime(nminus)):
                count += 1
                if (count >= n):
                    return nminus
            if (self.IsPrime(nplus)):
                count += 1
                if (count >= n):
                    return nplus
            k += 1

p = PE7()
print(p.NthPrime(10001))
