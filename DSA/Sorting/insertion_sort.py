#!usr/bin/env/python2
import os
import sys

def insertion_sort(seq):
	'''
	Implement insertion sorting, O(n**2)
	'''
	n = len(seq)
	for i in range(n-1):
		if seq[i]>seq[i+1]:
			seq[i],seq[i+1] = seq[i+1],seq[i]
		for j in range(i):
			for k in range(i):
				if seq[k]>seq[k+1]:
					seq[k],seq[k+1] = seq[k+1],seq[k]

	print seq


if __name__ == '__main__':
	
	seq = map(int,sys.argv[1:])
	insertion_sort(seq)