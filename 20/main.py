#! /usr/bin/python3.3
"""
    Project Euler #20
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

import math

def main():
    """
        Returns the solution to the problem
    """
    return sum(map(lambda x: int(x), str(math.factorial(100))))

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
