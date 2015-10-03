import math

def sieveOfEratosthenes(n):
	arr = [True]*n
	nSqrt = int(math.sqrt(n))

	for i in xrange(2,nSqrt):
		if arr[i] == True:
			for j in range(i**2,n,i):
				arr[j] = False
	
	return arr

def nthPrime(n,x):
	primes = sieveOfEratosthenes(x)
	count=0
	for i in xrange(2,x):
		if primes[i]==True:
			count+=1
			if count==n:
				return i

print nthPrime(10001,200000)