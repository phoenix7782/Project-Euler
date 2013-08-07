#! /usr/bin/python3.3
"""
	Project Euler #7
	Author: Robert McLaughlin
          <robert@sparkk.us>
	Consult LICENSE file for license.
"""

def is_prime(n):
	"""
		Checks to see if 'n' is prime.
		NOTE: because of the nature of prime numbers, this
		may get a bit slow
	"""
	if n <= 1: return False
	if n == 2: return True
	for check in range(2, n//2+1):
		if n%check == 0:
			return False
	return True

def get_primes():
	"""
		Yeilds a list of all prime numbers
		NOTE: because of the nature of prime numbers, this
		may get a bit slow
	"""
	n = 2
	while True:
		if is_prime(n):
			yield n
		n += 1

def main():
	"""
		Returns the solution to the problem
	"""
	i = 0
	for prime in get_primes():
		i += 1
		if i >= 10001:
			break
	return prime

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
