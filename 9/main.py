#! /usr/bin/python3.3
"""
	Project Euler #9
	Author: Robert McLaughlin
          <robert@sparkk.us>
	Consult LICENSE file for license.
"""

import math

def is_square(n):
	"""
		Returns True if the given number is a perfect square
		uses the idea that the sequence of perfect squares is
		the sum of the sequence of odds, ie
		[1, 1+3, 1+3+5, 1+3+5+7] -> [1, 4, 9, 16]
	"""
	n = int(n)
	last_odd = 1
	curr_sq = 1
	while curr_sq < n:
		last_odd += 2
		curr_sq += last_odd
		if curr_sq == n:
			return True
	return False

def main():
	"""
		Returns the solution to the problem
	"""
	TARGET_SUM = 1000
	# a < b
	for a in range(1, TARGET_SUM-2):
		for b in range(a, TARGET_SUM-1):
			# c^2 = a^2 + b^2
			c_sq = a**2 + b**2
			if is_square(c_sq):
				c = int(math.sqrt(c_sq))
				if a + b + c == 1000:
					return a*b*c
	return -1

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
