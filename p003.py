import math
n=600851475143

sq = int(math.sqrt(n))

if n%2 == 0:
	n=n/2
print 2
i=3
while i < sq:
	while n%i==0:
		n = n/i
		print i
	i+=2