#! /usr/bin/python3.3
"""
    Project Euler #17
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

mappings = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
   10 : 'Ten',
   11 : 'Eleven',
   12 : 'Twelve',
   13 : 'Thirteen',
   14 : 'Fourteen',
   15 : 'Fifteen',
   16 : 'Sixteen',
   17 : 'Seventeen',
   18 : 'Eighteen',
   19 : 'Nineteen',
   20 : 'Twenty',
   30 : 'Thirty',
   40 : 'Forty',
   50 : 'Fifty',
   60 : 'Sixty',
   70 : 'Seventy',
   80 : 'Eighty',
   90 : 'Ninety',
}

def letters(n):
    """
        Returns the number of letters in a given number n
    """
    phrase = ''
    # special case for one thousand
    if n == 1000:
        phrase = 'oneThousand'

    # handle the hundreds
    if 100 <= n < 1000:
        hundreds = n//100
        phrase += mappings[hundreds] + 'Hundred'
        # the phrase now looks like 'threehundred'
        n = n - hundreds*100
        # add an 'and' to allow for 'threehundredandtwentyfour'
        if n != 0:
            phrase += 'And'
    if 20 <= n < 100:
        tens = n//10
        phrase += mappings[tens*10]
        n -= tens*10
    if 10 <= n < 20:
        phrase += mappings[n]
        n = 0
    if 1 <= n < 10:
        phrase += mappings[n]
    return len(phrase)

def main():
    """
        Returns the solution to the problem
    """
    ret = 0
    for n in range(1, 1001):
        ret += letters(n)
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
