def fibo():
	a,b,s,su = 0,1,0,0
	while True:
		s=a+b
		a=b
		b=s
		if s>4000000:
			break
		if s%2==0:
			su+=s
	return su

print fibo()