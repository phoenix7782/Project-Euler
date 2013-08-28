#! /usr/bin/python3.3
"""
    Project Euler #21
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

# structured as {n : d(n), ... }
d_cache = [0]

def d(n):
    ret = 0
    for x in range(1, n):
        if n % x == 0:
            ret += x
    return ret

def gen_dcache():
    for n in range(1, 10000):
        d_cache.append(d(n))

def main():
    """
        Returns the solution to the problem
    """
    gen_dcache()
    ret = 0
    already_seen = []
    for a, d_a in enumerate(d_cache):
        for b, d_b in enumerate(d_cache):
            if a != b and d_a == b and d_b == a and not (b, a) in already_seen:
                ret += a
                ret += b
                already_seen.append((a, b))
    return ret

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
