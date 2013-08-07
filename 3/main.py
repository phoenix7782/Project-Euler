#! /usr/bin/python3.3
"""
	Project Euler #3
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
	# what is remaining of the original number
	# when a prime factor is found, this changes to the other factor
	remnants = 600851475143
	for prime in get_primes():
		if remnants % prime == 0:
			# we found a prime factor!
			remnants //= prime
			if is_prime(remnants):
				break
	return remnants

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
