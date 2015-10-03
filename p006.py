def sumOfSquares(n):
	return (n*(n+1)*(2*n+1))/6

def squaresOfSum(n):
	return ((n*(n+1))/2)**2

n=100
print squaresOfSum(n)-sumOfSquares(n)