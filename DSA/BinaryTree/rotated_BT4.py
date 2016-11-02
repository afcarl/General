#!usr/bin/env/python27
import sys


def rotated_BT(l):
	start = 0
	end = len(l)-1
	N = len(l)
	


	while (start<=end):
		mid = (start+end)/2
		next = (mid + 1)%N
		prev = (mid + N-1)%N
		print mid, next, prev

		if l[start]<=l[end]:
			print 'c1'

			return start

		elif ((l[mid]<=prev) & (l[mid]<=next)):
			print 'c2'
			return mid


		elif l[mid]>=l[start]:
			print 'c3'
			start = mid + 1

		elif l[mid]<=l[end]:
			print 'c4'
			end = mid-1






if __name__ == '__main__':
	l = map(lambda x: int(x),sys.argv[1:])
	print l
	#l = sorted(l)

	print rotated_BT(l)