#!usr/bin/env/python2
import os
import sys

def selection_sort(seq):
	'''
	Implement selection sorting, O(n**2)
	'''
	n = len(seq)
	for i in range(n-1):
		
		for j in range(i,n-1):
			
			if seq[i]>seq[j+1]:
				seq[i],seq[j+1] = seq[j+1],seq[i]

	print seq


if __name__ == '__main__':
	
	seq = map(int,sys.argv[1:])
	selection_sort(seq)