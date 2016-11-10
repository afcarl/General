#!usr/bin/env/python2
#Source : http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

import os
import sys

def merge_sort(seq):
	'''
	implement merge sort algorithm :
	- Divide and Conquer
	- Recursive
	- Stable
	- Space Complexity: O(n) Not in place
	- Time Complexity: O(n * log n) 
	'''
	n = len(seq)
	if n>1:
		
		mid = n//2
		L = seq[:mid]
		
		R = seq[mid:]
		
		merge_sort(L)
		merge_sort(R)
	
		nL = len(L)
		nR = len(R)
		i = 0
		j = 0
		k = 0
		while i<nL and j<nR:
			if (L[i] < R[j]):
				seq[k] = L[i]
				i = i+1

			else:
				seq[k] = R[j]
				j = j+1
			k = k+1

		while i<nL:
			
			seq[k] = L[i]
			k = k+1
			i = i+1

		while j<nR:
			
			seq[k] = R[j]
			k = k+1
			j = j+1

	#print("Merging ",seq)



if __name__ == '__main__':
	seq = map(int,sys.argv[1:])
	merge_sort(seq)
	print seq