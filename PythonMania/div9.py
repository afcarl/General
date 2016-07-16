import numpy as np 
import random
import time

def digit_sum(a):

    if a== 0:
        return 0



    return a % 10 + digit_sum(a/10)


def byNine(n):
	print n
	while True:
		
		n1 = digit_sum(n)
		n = n1
		if n1<=9:
			
			if n1==9:
				print 'is divisble by'

			else:
				print 'not divisble by 9'

			break


tic = time.clock()

#check_numbers = random.sample(range(10000000),10)
# below instead of the number you can replace with check_numbers
map(lambda x: byNine(x), (1223333,))
tic1 = time.clock()
print (tic1- tic)

tic = time.clock()
if 1223333%2!=0:
	print 'not divisble by 9'

else:
	print 'divisble'
tic1 = time.clock()
print (tic1 - tic)
