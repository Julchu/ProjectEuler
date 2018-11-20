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

def Q2():
	"""
	Def: sum of even fibonacci under 4,000,000
	Run: print(Q2())
	"""
	fib = [0, 1]
	sum = 0
	i = 1
	while fib[i] < 4000000:
		fib.append(fib[i] + fib[i-1])
		if fib[i] % 2 == 0:
			sum += fib[i]
		i += 1
	return sum

def Q3():