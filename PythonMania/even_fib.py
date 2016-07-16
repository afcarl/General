tot = 4000000
a = 1
b = 2
s = 0
es = []
es.append(1)
es.append(2)

def create_fib(a,b):
	#if s < tot:
	print a,b , 'a,b'
	s = a+b
	es.append(s)
	#print s
	# if (a%2 == 0 and b%2 == 0):
	# 	es = a+b
	# 	print es

	a = b
	b = s
	return a,b,s


while s<tot:
	a,b,s = create_fib(a,b)

es = filter(lambda x: x%2==0, es)
print sum(es)
