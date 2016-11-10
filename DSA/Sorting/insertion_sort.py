#!usr/bin/env/python2
import os
import sys

def insertion_sort(seq):
	'''
	Implement insertion sorting, O(n**2)
	'''
	n = len(seq)
	for i in range(1,n):
		# Start from index one in the right unsorted list for comparision with the left sorted list, 
		#  As the left sorted list begins with one element in it which is always sorted
		j = i # index of the new number to be inserted
		k = i-1 # Immediate left value to the new "to be inserted element"
		while j>0 and k>=0:
			# j will go minimum to 1 and k to 0 as its the value in the left sorted value
			if seq[j]<seq[k]:
				seq[k],seq[j] = seq[j],seq[k] # swap the values
				j = k
				k = k-1
			else:
				break

	print seq


if __name__ == '__main__':
	
	seq = map(int,sys.argv[1:])
	insertion_sort(seq)