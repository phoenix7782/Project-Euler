#! /usr/bin/python3.3
"""
	Project Euler #6
	Author: Robert McLaughlin
          <robert@sparkk.us>
	Consult LICENSE file for license.
"""

def main():
	"""
		Returns the solution to the problem
	"""
	n_1 = 1
	n_n = 100
	# find the square of the sum of all numbers (the quick way)
	S_n_sq = ( (n_1 + n_n)/2 * (n_n - n_1 + 1) ) ** 2
	# subtract off each square
	ret = S_n_sq
	for n in range(n_1, n_n+1):
		ret -= n**2
	return int(ret)

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
