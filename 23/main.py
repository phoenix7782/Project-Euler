#! /usr/bin/python3.3
"""
    Project Euler #<>
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

def get_sum_divisors(n):
    ret = 0
    for x in range(1, n):
        if n % x == 0:
            ret += x
    return ret

def is_abundant(n):
    return n > get_sum_divisors(n)

def get_abundant_numbers():
    ret = []
    for n in range(2, 28124):
        if is_abundant(n):
            ret.append(n)
    return tuple(ret)

def can_be_represented(numbers, n):
    """
        return True if n can be represented by the sum of two different 
        numbers from 'numbers'
    """
    ret = False
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == n and n1 != n2:
                ret = True
                break
            elif n2 > n:
                continue
            elif n1 > n:
                break
    return ret

def get_sum():
    ret = 0
    print("generating numbers")
    numbers = get_abundant_numbers()
    print("checking sums")
    for x in range(1, 28124):
        print(x/28124*100//1)
        if can_be_represented(numbers, x):
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
