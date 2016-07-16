import numpy as np 

div_l = []
n = 600851475143
div = 0
i = 1
while True:
	
	if n%2 == 0:
		n = n/2
		div_l.append(2)
		if n ==1 :
			break
	if n%3 == 0:
		n = n/3
		div_l.append(3)
		if n ==1 :
			break
	
	t1 = 6*i - 1
	t2 = 6*i + 1
	
	if n%t1 == 0:
		n = n/t1
		div_l.append(t1)
		if n == 1 :
			break
	if n%t2 == 0:
		n = n/t2
		div_l.append(t1)
		if n ==1 :
			break
	i = i+1


print max(div_l)

