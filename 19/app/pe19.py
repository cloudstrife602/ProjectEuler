"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime


class PE19(object):

    def isLeapYear(self, year):
        allowed_types = (int, float, complex)
        if (isinstance(year, allowed_types) == 0):
            raise ValueError
        else:
            if (year % 400 == 0):
                # century divisible by 400
                return 1
            elif (year % 100 == 0):
                # century
                return 0
            elif (year % 4 == 0):
                # leap year
                return 1
            else:
                # regular year
                return 0

    def daysInMonth(self, month, year):
        allowed_types = (int, float, complex)
        if (isinstance(month, allowed_types) == 0
                or isinstance(year, allowed_types) == 0
                or month < 1
                or month > 12
                or year < 0):
            raise ValueError
        else:
            leapYear = self.isLeapYear(year)
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return 31
            elif (month == 2):
                if (leapYear):
                    return 29
                else:
                    return 28
            elif month in [4, 6, 9, 11]:
                return 30
            else:
                raise ValueError

    def dayIs(self, day, month, year):
        allowed_types = (int, float, complex)
        if (isinstance(day, allowed_types)
                and isinstance(month, allowed_types)
                and isinstance(year, allowed_types)
                and year >= 1
                and year <= 9999
                and month >= 1
                and month <= 12
                and day >= 1
                and day <= self.daysInMonth(month, year)):
            d = datetime.date(year, month, day)
            return d.weekday()
        else:
            raise ValueError

p = PE19()
sum_of_sundays = 0
# iterate over years in 20th century
for year in range(1901, 2001):
    # iterate over months in the year
    for month in range(1, 13):
        # iterate over days in the month
        if (p.dayIs(1, month, year) == 6):
            sum_of_sundays += 1

print(sum_of_sundays)
