#! /usr/bin/python3.3
"""
	Project Euler #1
	Author: Robert McLaughlin
          <robert@sparkk.us>
	Consult LICENSE file for license.
"""

def main():
	"""
		Returns the solution to the problem
	"""
	cumsum = 0
	for num in range(1, 1000):
		if num % 3 == 0 or num % 5 == 0:
			cumsum += num
	return cumsum

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
