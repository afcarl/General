#!usr/bin/env/python27

import sys

def find_element(l,a):
	start = 0
	end = len(l) - 1

	while(start<=end):
		mid = (start+end)/2
		if l[mid] == a:
			return mid

		elif l[mid]<=l[end]:
			if ((l[mid]<=a) & (l[end]>=a)):
				start = mid + 1
			else:
				end = mid - 1

		elif l[mid]>=l[start]:
			if ((a<=l[mid]) & (a>=l[start])):
				end = mid - 1
			else:
				start = mid + 1





if __name__ == '__main__':

	l = map(lambda x: int(x),sys.argv[1:])
	print l
	#l = sorted(l)
	a = int(raw_input("Enter element: \n"))

	print find_element(l,a)

