import math

def sieveOfEratosthenes(n):
	arr = [True]*n
	nSqrt = int(math.sqrt(n))

	for i in xrange(2,nSqrt):
		if arr[i] == True:
			for j in range(i**2,n,i):
				arr[j] = False
	
	return arr

def sumOfPrimes(n):
	primes = sieveOfEratosthenes(n)
	sum = 0
	for i in xrange(2,n):
		if primes[i]==True:
			sum+=i
	return sum

n=2000000
print sumOfPrimes(n)