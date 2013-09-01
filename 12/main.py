#! /usr/bin/python3
"""
    Project Euler #12
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""
import math

def num_divisors(n):
    ret = 0
    for x in range(1, int(math.sqrt(n))+1):
        if n%x == 0:
            ret += 2
    return ret

def main():
    """
        Returns the solution to the problem
    """
    triangle = 0
    last_num = 0
    while True:
        last_num += 1
        triangle += last_num
        n_div = num_divisors(triangle)
        if n_div > 500:
            break
    return triangle

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
