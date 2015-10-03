def largestPalin():
	arr = []
	for x in xrange(100,999):
		for y in xrange(100,999):
			z = x*y
			if str(z)==str(z)[::-1]:
				arr.append(z)
	return max(arr)

print largestPalin()