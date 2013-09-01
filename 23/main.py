#! /usr/bin/python3.3
"""
    Project Euler #23
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

import math

def get_sum_divisors(n):
    """
        Get the sum of all divisors of 'n'
    """
    ret = 1
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            ret += x
            if n/x != x:
                ret += n/x
    return ret

def is_abundant(n):
    """
        Returns True if n is abundant, otherwise
        returns False
    """
    return n < get_sum_divisors(n)

def get_abundant_numbers(i, j):
    """
        Get a set of all abundant numbers on the 
        interval [i, j]
    """
    ret = []
    for n in range(i, j):
        if is_abundant(n):
            ret.append(n)
    return set(ret)

def can_be_represented(numbers, n):
    """
        return True if n can be represented by the sum of two different 
        numbers from 'numbers'
        'numbers' is a set of nonnegative numbers
    """
    return any( (n-abn in numbers) for abn in numbers)

def get_sum():
    ret = 0
    numbers = get_abundant_numbers(2, 28124)
    for x in range(1, 28124):
        if not can_be_represented(numbers, x):
            ret += x
    return ret

def main():
    """
        Returns the solution to the problem
    """
    return get_sum()

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
