def specialTriplet(sum):
	for i in xrange(1,sum/3):
		for j in xrange(i,sum/2):
			c=sum-i-j
			if i*i+j*j==c*c:
				return (i*j*c)

sum=1000
print specialTriplet(sum)