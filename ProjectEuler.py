# Project Euler

def Q1(n):
	"""
		Def: sum of multiples of 3 or 5 under 1000
		Run: print(Q1(1000))
	"""
	sum = 0
	i = 0
	while i < n:
		if i % 3 == 0 or i % 5 == 0:
			sum += i
		i += 1
	return sum

def Q2(n):
	"""
		Def: sum of even fibonacci under 4,000,000
		Run: print(Q2(4000000))
	"""
	fib = [0, 1]
	sum = 0
	i = 1
	while fib[i] < n:
		fib.append(fib[i] + fib[i-1])
		if fib[i] % 2 == 0:
			sum += fib[i]
		i += 1
	return sum

import math
def Q3(n):
	"""
		Def: largest prime factor of 600851475143
		Run: print(Q3(600851475143))
	"""
	factors = []
	primes = []
	prime = True
	# Find biggest factor of n
	end = n - 1
	while end > math.sqrt(n) and len(primes) < 1:
		if n % end == 0:	
			if end == 1 or end == 2:
				primes.append(end)
			else:
				# Checking if number is prime
				prime = True
				factor = end
				while prime and factor > math.sqrt(end):
					if end % factor == 0:
						prime = False
					factor -= 1
				if prime:
					primes.append(end)
		end -= 1
	if len(primes) > 0:
		return primes
	elif prime:
		primes = n
	else:
		primes = None
	return primes
	# Find biggest prime factor of n
	# return primes.pop()
	
print(Q3(20))