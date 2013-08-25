#! /usr/bin/python3.3
"""
    Project Euler #14
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

def chain_len(n):
    """
        Using 'n' as the starting number, this is the length of the collatz sequence
    """
    ret = 0
    while n > 1:
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n+1
        ret += 1
    return ret

def main():
    """
        Returns the solution to the problem
    """
    biggest_chain   = -1
    biggest_chain_n = -1
    for n in range(1000000):
        n_len = chain_len(n)
        if n_len > biggest_chain:
            biggest_chain = n_len
            biggest_chain_n = n
    return biggest_chain_n

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
