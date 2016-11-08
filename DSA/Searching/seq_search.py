#!usr/bin/env/python2

import os
import sys

def sequential_search(A,a):
	'''
	Perform simple sequential_search to find an element in A (linear Data structure eg: list/array)
	*** If element is present in A ***
	Best Case: O(1)
	Average Case: O(n/2)
	Worst Case: O(n)

	*** If element not present in A ***
	Best Case: O(n)
	Average Case: O(n)
	Worst Case: O(n)
	'''

	n = len(A)

	for i in range(n):
		if A[i] == a:
			return True

	return False

if __name__ == '__main__':
	A = map(int, sys.argv[1:])
	a = int(raw_input("Enter element to find \n"))

	print sequential_search(A,a)