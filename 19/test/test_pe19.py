import unittest
from app.pe19 import PE19

class TestPE19(unittest.TestCase):

    def setUp(self):
        self.d = PE19()

    def test_isLeapYear_not_a_year(self):
        d = self.d
        self.assertRaises(ValueError, d.isLeapYear, 'three')

    def test_isLeapYear_not_leap_year(self):
        d = self.d
        self.assertEqual(d.isLeapYear(1901), 0)

    def test_isLeapYear_is_leap_year(self):
        d = self.d
        self.assertEqual(d.isLeapYear(1904), 1)

    def test_isLeapYear_century_divisible_by_400(self):
        d = self.d
        self.assertEqual(d.isLeapYear(2000), 1)

    def test_isLeapYear_century_not_divisible_by_400(self):
        d = self.d
        self.assertEqual(d.isLeapYear(1900), 0)

    def test_daysInMonth_not_a_year(self):
        d = self.d
        self.assertRaises(ValueError, d.daysInMonth, 1, 'three')

    def test_daysInMonth_not_a_month(self):
        d = self.d
        self.assertRaises(ValueError, d.daysInMonth, 'first', 1900)

    def test_daysInMonth_not_a_month_or_year(self):
        d = self.d
        self.assertRaises(ValueError, d.daysInMonth, 'first', 'three')

    def test_daysInMonth_invalid_month(self):
        d = self.d
        self.assertRaises(ValueError, d.daysInMonth, -1, 1900)

    def test_daysInMonth_invalid_year(self):
        d = self.d
        self.assertRaises(ValueError, d.daysInMonth, 1, -1)

    def test_daysInMonth_regular_year(self):
        d = self.d
        # check regular year
        year = 1901
        self.assertEqual(d.daysInMonth(1, year), 31)
        self.assertEqual(d.daysInMonth(2, year), 28)
        self.assertEqual(d.daysInMonth(3, year), 31)
        self.assertEqual(d.daysInMonth(4, year), 30)
        self.assertEqual(d.daysInMonth(5, year), 31)
        self.assertEqual(d.daysInMonth(6, year), 30)
        self.assertEqual(d.daysInMonth(7, year), 31)
        self.assertEqual(d.daysInMonth(8, year), 31)
        self.assertEqual(d.daysInMonth(9, year), 30)
        self.assertEqual(d.daysInMonth(10, year), 31)
        self.assertEqual(d.daysInMonth(11, year), 30)
        self.assertEqual(d.daysInMonth(12, year), 31)

    def test_daysInMonth_regular_leapyear(self):
        d = self.d
        year = 1904
        self.assertEqual(d.daysInMonth(1, year), 31)
        self.assertEqual(d.daysInMonth(2, year), 29)
        self.assertEqual(d.daysInMonth(3, year), 31)
        self.assertEqual(d.daysInMonth(4, year), 30)
        self.assertEqual(d.daysInMonth(5, year), 31)
        self.assertEqual(d.daysInMonth(6, year), 30)
        self.assertEqual(d.daysInMonth(7, year), 31)
        self.assertEqual(d.daysInMonth(8, year), 31)
        self.assertEqual(d.daysInMonth(9, year), 30)
        self.assertEqual(d.daysInMonth(10, year), 31)
        self.assertEqual(d.daysInMonth(11, year), 30)
        self.assertEqual(d.daysInMonth(12, year), 31)

    def test_daysInMonth_century_leapyear(self):
        d = self.d
        year = 1900
        self.assertEqual(d.daysInMonth(1, year), 31)
        self.assertEqual(d.daysInMonth(2, year), 28)
        self.assertEqual(d.daysInMonth(3, year), 31)
        self.assertEqual(d.daysInMonth(4, year), 30)
        self.assertEqual(d.daysInMonth(5, year), 31)
        self.assertEqual(d.daysInMonth(6, year), 30)
        self.assertEqual(d.daysInMonth(7, year), 31)
        self.assertEqual(d.daysInMonth(8, year), 31)
        self.assertEqual(d.daysInMonth(9, year), 30)
        self.assertEqual(d.daysInMonth(10, year), 31)
        self.assertEqual(d.daysInMonth(11, year), 30)
        self.assertEqual(d.daysInMonth(12, year), 31)

    def test_daysInMonth_century_400_leapyear(self):
        d = self.d
        year = 2000
        self.assertEqual(d.daysInMonth(2, year), 29)
        self.assertEqual(d.daysInMonth(3, year), 31)
        self.assertEqual(d.daysInMonth(4, year), 30)
        self.assertEqual(d.daysInMonth(5, year), 31)
        self.assertEqual(d.daysInMonth(6, year), 30)
        self.assertEqual(d.daysInMonth(7, year), 31)
        self.assertEqual(d.daysInMonth(8, year), 31)
        self.assertEqual(d.daysInMonth(9, year), 30)
        self.assertEqual(d.daysInMonth(10, year), 31)
        self.assertEqual(d.daysInMonth(11, year), 30)
        self.assertEqual(d.daysInMonth(12, year), 31)

    def test_dayIs_invalid_day(self):
        d = self.d
        self.assertRaises(ValueError, d.dayIs, 0, 1, 1900)
        self.assertRaises(ValueError, d.dayIs, 32, 1, 1900)
        self.assertRaises(ValueError, d.dayIs, 30, 2, 1904)
        self.assertRaises(ValueError, d.dayIs, 29, 2, 1901)

    def test_dayIs_not_a_day(self):
        d = self.d
        self.assertRaises(ValueError, d.dayIs, 'dummy', 1, 1900)

    def test_dayIs_invalid_month(self):
        d = self.d
        self.assertRaises(ValueError, d.dayIs, 1, 0, 1900)
        self.assertRaises(ValueError, d.dayIs, 1, 13, 1900)

    def test_dayIs_not_a_month(self):
        d = self.d
        self.assertRaises(ValueError, d.dayIs, 1, 'dummy', 1900)

    def test_dayIs_invalid_year(self):
        d = self.d
        self.assertRaises(ValueError, d.dayIs, 1, 1, 0)
        self.assertRaises(ValueError, d.dayIs, 1, 1, 10000)
        self.assertRaises(ValueError, d.dayIs, 1, 1, -1)

    def test_dayIs_not_a_year(self):
        d = self.d
        self.assertRaises(ValueError, d.dayIs, 1, 1, "dummy")

    def test_dayIs(self):
        d = self.d
        self.assertEqual(d.dayIs(1, 1, 1900), 0)
        self.assertEqual(d.dayIs(2, 1, 1900), 1)
        self.assertEqual(d.dayIs(3, 1, 1900), 2)
        self.assertEqual(d.dayIs(4, 1, 1900), 3)
        self.assertEqual(d.dayIs(5, 1, 1900), 4)
        self.assertEqual(d.dayIs(6, 1, 1900), 5)
        self.assertEqual(d.dayIs(7, 1, 1900), 6)


if __name__ == '__main__':
    unittest.main()
