#! /usr/bin/python3
"""
    Project Euler #39
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

def isqrt(n):
    """
        Newton's method for finding an integer square root
    """
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def has_a_solution(p):
    """
        returns true if the given perimeter, 'p', can be
        represented by coprime integer sides of a right-triangle. That is,
        a+b+c=p, where a, b, and c are coprime integers.

        Proof:

        using Euclid's formula,
        a = (m^2 - n^2)
        b = (2mn)
        c = (m^2 + n^2)
        for coprime m and n

        a + b + c = p
        (m^2 - n^2) + (2mn) + (m^2 + n^2) = p
        2*m^2 + 2mn = p
        2m(m+n)=p
        2(m/n)(m/n+1)=p

        for rational k, k = m/n
        2k(k+1)=p
        2k^2 + 2k - p = 0
            -2 +- sqrt(4-4(2)(-p))
        k = ----------------------
                      2(2)
        
             -2 += sqrt(1+2p)
        k =  -----------------
                    2

        Therefore, for 'k' to be rational, sqrt(1+2p) must be an integer
    """
    return isqrt(1+2*p)**2 == (1+2*p)

def main():
    """
        Returns the solution to the problem
    """
    nums = [] # at index i-1, contains the number of integer triangles
              # for a perimeter of i
    # initialize to zero
    for i in range(1000):
        nums.append(0)

    # iterate over each perimeter 'p'
    for p in range(1, 1000+1):
        # if p has a solution, mark that solution and all multiples of it
        if has_a_solution(p):
            mult = 1
            while mult*p <= 1000:
                nums[mult*p-1] += 1
                mult += 1

    # find the index with the highest value
    best_i = 0
    best_p = 0
    for i, p in enumerate(nums):
        if p > best_p:
            best_i = i
            best_p = p
    
    # return, shifting back to 1-based
    return 1+best_i

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
