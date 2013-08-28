#! /usr/bin/python3.3
"""
    Project Euler #19
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

import datetime

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)
ONE_WEEK = datetime.timedelta(days=7)
MONTHS_WITH_THIRTY     = [9, 4,  6, 11]
MONTHS_WITH_THIRTY_ONE = [1, 3, 5, 7, 8, 10, 12]
FEBRUARY               = 2

def is_firstsunday(year, day_of_month, day_of_week):
    """
        Year is the full four-digit year number
        day_of_month is the 1-indexed day of the month, for example 3
        day_of_week is MON, TUE, WED, etc ...
    """
    return year > 1900 and day_of_week == SUN and day_of_month == 1

def is_leapyear(year):
    return (year % 4 == 0) and (not year % 100 == 0 or year % 400 == 0)

def is_leapday(year, day):
    """
        returns True if this is a leap day (ie february 29th, on a leap year)
        if an invalid day is supplied, (ie february 29th on non-leap year) returns False
    """
    return is_leapyear(year) and day == 29

def get_sundays():
    ret = 0
    curr_year = 1900
    curr_month = 1
    curr_day = 1
    day_of_week = MON
    # this loop runs once for each day
    while curr_year < 2001:
        # if this is a first sunday, increment ret
        if is_firstsunday(curr_year, curr_day, day_of_week):
            ret += 1
        # perform the increment of the day
        day_of_week += 1
        day_of_week %= 7
        curr_day += 1
        # advance the months / years if needed
        if curr_day > 30 and curr_month in MONTHS_WITH_THIRTY:
            curr_day = 1
            curr_month += 1
        elif curr_day > 31 and curr_month in MONTHS_WITH_THIRTY_ONE:
            curr_day = 1
            if curr_month == 12:
                curr_year += 1
                curr_month = 1
            else:
                curr_month += 1
        # handle leap years / february
        elif curr_day > 28 and curr_month == FEBRUARY:
            if not is_leapday(curr_year, curr_day):
                curr_month += 1
                curr_day = 1
    return ret

def main():
    """
        Returns the solution to the problem
    """
    return get_sundays()

if __name__ == '__main__':
    import time
    start = time.time()
    
    print("Solution: {0:,d}".format(main()))
    
    diff = time.time() - start
    if diff < 1:
        print("Took {0:.4f} milliseconds".format(diff*1000))
    elif diff < 60:
        print("Took {0:.4f} seconds".format(diff))
    elif diff < 360:
        print("Took {0:.4f} minutes".format(diff/60))
    else:
        print("Took {0:.4f} hours".format(diff/60/60))
