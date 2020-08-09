"""
Question - Check if a year is a leap year or not.
"""


def check_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a leap year")


check_leap(int(2000))
