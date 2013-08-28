#! /usr/bin/python3.3
"""
    Project Euler #18
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

TRIANGLE  = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

# paths_cache = {row: {index: weight, ...}, ... }
paths_cache = {}

def add_to_cache(row, i, weight):
    if not row in paths_cache:
        paths_cache[row] = {}
    paths_cache[row][i] = weight

def get_from_cache(row, i):
    """
        Gets the largest weighted path value starting at this coord
        from the cache. If this path has not been calculated, returns None
    """
    if row in paths_cache:
        if i in paths_cache[row]:
            return paths_cache[row][i]
    return None

def best_path(row=0, i=0):
    # base case
    if row == len(TRIANGLE)-1: return TRIANGLE[row][i]
    
    # check the cache
    ret = get_from_cache(row, i)
    if ret:
        return ret
    else:
        ret = TRIANGLE[row][i]
    
    # compute manually
    left  = best_path(row+1, i)
    right = best_path(row+1, i+1)
    ret += max(left, right)
    
    add_to_cache(row, i, ret)    
    
    return ret

def main():
    """
        Returns the solution to the problem
    """
    return best_path()

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
