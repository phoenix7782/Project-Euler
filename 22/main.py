#! /usr/bin/python3.3
"""
    Project Euler #22
    Author: Robert McLaughlin
          <robert@sparkk.us>
    Consult LICENSE file for license.
"""

names = []

def load_names():
    global names
    names_f = open('names.txt')
    str_names = names_f.read()
    names_f.close()
    new_names = str_names.split(",")
    for name in new_names:
        names.append(name[1:-1])
    names = sorted(names)

def calc_name_score(name):
    """
        Calculates the name score based on characters, not position
    """
    ret = 0
    for char in name:
        ret += ord(char) - ord('A') + 1
    return ret

def calc_total_score():
    ret = 0
    for i, name in enumerate(names):
        ret += (i+1) * calc_name_score(name)
    return ret

def main():
    """
        Returns the solution to the problem
    """
    load_names()
    return calc_total_score()

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
