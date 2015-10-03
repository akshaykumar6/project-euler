def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

def lcm(a,b):
	return (a*b)/gcd(a,b)

def smallestMultiple(n):
	a=1
	for i in range(2,n+1):
		a=lcm(a,i)
	return a

print smallestMultiple(20)