#! /usr/bin/python3.3
"""
	Project Euler #10
	Author: Robert McLaughlin
          <robert@sparkk.us>
	Consult LICENSE file for license.
"""

import math

def gen_sievegrid():
	"""
		Returns a number that represents a sieve grid where
		000010 indicates that 2 is not a prime, and 
		001111 indicates that 1,2,3,4 are not prime
	"""
	grid = 0b0011 # 1 and 0 are not a prime, ignore them by default
	for i in range(int(math.sqrt(2000000))+1):
		# if this is a prime
		if not ((grid >> i) & 0x01):
			# make all bits corresponding to multiples equal to 1
			for multiple in range(i*2, 2000001, i):
				grid |= 1 << multiple
	return grid

def sum_primes(grid):
	"""
		Sum up all of the primes in this grid up to
		2000000
	"""
	ret = 0
	for i in range(2000001):
		if not ((grid >> i) & 0x01):
			ret += i
	return ret

def main():
	"""
		Returns the solution to the problem
	"""
	return sum_primes(gen_sievegrid())

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
