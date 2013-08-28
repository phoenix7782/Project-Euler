#! /usr/bin/python3.3
"""
    Project Euler #15
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

SIZE = 20

# path_cache is {deltaX : {deltaY : paths}, ...}
# this way similar path traversals can be skipped
path_cache = {}

def is_in_bounds(x, y):
    """
        Returns True if x and y are on the interval [0, SIZE]
    """
    return 0 <= x <= SIZE and 0 <= y <= SIZE

def get_from_cache(x,y):
    """
        Get the number of paths from (x,y) to the target from the cache
        if they do not exist in the cache yet, None is returned
    """
    deltaX = SIZE - x
    deltaY = SIZE - y
    if deltaX in path_cache:
        if deltaY in path_cache[deltaX]:
            return path_cache[deltaX][deltaY]
    return None

def store_in_cache(x, y, paths):
    """
        Store the number of paths to the target that were discovered
        from the coordinate (x,y) in the cache to avoid recalculating
    """
    deltaX = SIZE - x
    deltaY = SIZE - y
    if not deltaX in path_cache:
        path_cache[deltaX] = {}
    path_cache[deltaX][deltaY] = paths

def count_paths(x,y):
    """
        Count the number of paths from a given coordinate to another
        coordinate.
    """
    # base case: if at the target
    if x == SIZE and y == SIZE: return 1
    
    # check the cache and return from that if exists
    ret = get_from_cache(x,y)
    if ret: 
        return ret
    else:
        ret = 0

    # find the path the hard way
    if is_in_bounds(x + 1, y):
        ret += count_paths(x+1, y)
    if is_in_bounds(x, y + 1):
        ret += count_paths(x, y+1)
    
    # cache the result
    store_in_cache(x, y, ret)
    return ret

def main():
    """
        Returns the solution to the problem
    """
    return count_paths(0,0)

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
