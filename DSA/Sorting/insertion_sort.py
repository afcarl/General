#!usr/bin/env/python2
import os
import sys

def insertion_sort(seq):
	'''
	Implement insertion sorting, O(n**2)
	'''
	n = len(seq)
	for i in range(1,n):
		j = i
		k = i-1
		while j>0 and k>=0:
			if seq[j]<seq[k]:
				seq[k],seq[j] = seq[j],seq[k]
				j = k
				k = k-1
			else:
				break

				j = j-1

	print seq


if __name__ == '__main__':
	
	seq = map(int,sys.argv[1:])
	insertion_sort(seq)