"""Describe Test class for PE7."""
import unittest
from app.pe7 import PE7


class TestPE7(unittest.TestCase):
    """Describe tests for PE7."""

    def setUp(self):
        """Set up for test."""
        self.p = PE7()

    def test_prime_less_than_one_is_invalid(self):
        """Only valid for positive integers."""
        p = self.p
        self.assertRaises(ValueError, p.IsPrime, 0)

    def test_prime_1_is_not_prime(self):
        """One is never prime."""
        p = self.p
        self.assertEqual(p.IsPrime(1), False)

    def test_prime_2_is_prime(self):
        """Two is the only even prime."""
        p = self.p
        self.assertEqual(p.IsPrime(2), True)

    def test_prime_3_is_prime(self):
        """Three is prime."""
        p = self.p
        self.assertEqual(p.IsPrime(3), True)

    def test_prime_evens_are_not_prime(self):
        """Even numbers are not prime."""
        p = self.p
        for n in range(4, 100, 2):
            self.assertEqual(p.IsPrime(n), False)

    def test_prime_multiples_of_3_are_not_prime(self):
        """Any multiple of three are not prime."""
        p = self.p
        for n in range(6, 100, 3):
            print("Testing: " + str(n))
            self.assertEqual(p.IsPrime(n), False)

    def test_prime_square_numbers_are_not_prime(self):
        """If a number is square, it cannot be prime."""
        p = self.p
        for n in range(1, 100):
            print(n)
            self.assertEqual(p.IsPrime(n*n), False)

    def test_prime_known_large_primes_are_prime(self):
        """Known large primes are prime."""
        p = self.p
        for n in {23}:
            self.assertEqual(p.IsPrime(n), True)

    def test_nth_prime_2_is_the_first_prime(self):
        """Two is the first prime."""
        p = self.p
        self.assertEqual(p.NthPrime(1), 2)

    def test_nth_prime_13_is_the_sixth_prime(self):
        """Thirteen is the sixth prime."""
        p = self.p
        self.assertEqual(p.NthPrime(6), 13)

if __name__ == '__main__':
    unittest.main()
