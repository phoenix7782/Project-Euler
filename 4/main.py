#! /usr/bin/python3.3
"""
	Project Euler #4
	Author: Robert McLaughlin
          <robert@sparkk.us>
	Consult LICENSE file for license.
"""

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]

def main():
	"""
		Returns the solution to the problem
	"""
	largest = -1
	for n1 in range(100, 1000):
		for n2 in range(n1, 1000):
			n = n1 * n2
			if is_palindrome(n):
				largest = max(largest, n)
	return largest

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
