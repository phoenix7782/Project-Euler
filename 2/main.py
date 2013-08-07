#! /usr/bin/python3.3
"""
	Project Euler #2
	Author: Robert McLaughlin
          <robert@sparkk.us>
	Consult LICENSE file for license.
"""

def main():
	"""
		Returns the solution to the problem
	"""
	UPPER_LIMIT = 4000000 # four million
	# uses a sliding window where [1, 1, 2, ... n_2, n_1]
	n_2 = 1
	n_1 = 1
	cumsum = 0
	while n_1 <= UPPER_LIMIT:
		if n_1 % 2 == 0:
			cumsum += n_1
		tmp = n_2 + n_1
		n_2 = n_1
		n_1 = tmp	
	
	return cumsum

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
