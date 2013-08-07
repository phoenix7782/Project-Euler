#! /usr/bin/python3.3
"""
	Project Euler #5
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

def prime_factorize(n):
	"""
		Returns a tuple of the prime factorization
		of the number n in least-to-greatest order
	"""
	remaining = n
	ret = []
	for x in range(1, n//2+1):
		if is_prime(x):
			while remaining % x == 0:
				remaining //= x
				ret.append(x)
	if remaining > 1:
		ret.append(remaining)
	return tuple(ret)

def factors_missing(factors, test):
	"""
		Given factors and test, makes sure all
		elements of test are represented in factors,
		including repeats. Returns a tuple of elements
		not found
	"""
	ret = []
	i = 0
	for factor in test:
		try:
			i = factors.index(factor, i) + 1
		except ValueError:
			ret.append(factor)
	return tuple(ret)

def main():
	"""
		Returns the solution to the problem
	"""
	ret = 1
	# a list of the factors already in the result
	factors = []
	# go through [1, 20) and make sure all prime factors of each number
	# are in the result. If not, put the factor into the result
	for x in range(1, 20):
		pf = prime_factorize(x)
		for missing in factors_missing(factors, pf):
			factors.append(missing)
			ret *= missing
	return ret

if __name__ == '__main__':
	print("Solution: {0:,d}".format(main()))
