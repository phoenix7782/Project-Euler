#! /usr/bin/python3
"""
    Project Euler #24
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

def permute(l):
    """
        Assuming l is sorted, generates lexicographic
        permutations of l
    """
    if not l: yield []
    else:
        for i in range(len(l)):
            cpy = list(l)
            n = cpy.pop(i)
            for sub in permute(cpy):
                yield [n] + sub

def main():
    """
        Returns the solution to the problem
    """
    n = 0
    ret = []
    for permutation in permute([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        n += 1
        if n == 1000000:
            ret = permutation
            break
    new_ret = 0
    for i, n in enumerate(ret):
        new_ret += 10**(len(ret) - i -1) * n
    return new_ret

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
