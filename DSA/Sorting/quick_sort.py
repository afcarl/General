#!usr/bin/env/python2
# source: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html
import os
import sys


def quick_sort(A):
	'''
	implement quick sort algorithm
	- Divide and conquer
	- Recursive
	- Not stable
	- Avg Case: O(n * log n)
	- Worst case: O(n ** 2)
	'''
	quick_sort_helper(A,0,len(A)-1)


def quick_sort_helper(A,first,last):
	if first<last:
		pIndex = partition(A,first,last)
		quick_sort_helper(A,first,pIndex-1)
		quick_sort_helper(A,pIndex+1,last)

def partition(A,first,last):
	pivotvalue = A[first]
	leftmark = first+1
	rightmark = last

	done = False
	while not done:

		while leftmark <= rightmark and A[leftmark] <= pivotvalue :
			leftmark += 1

		while rightmark >= leftmark and A[rightmark] >= pivotvalue:
			rightmark -= 1

		if rightmark < leftmark:
			done = True

		else:
			A[leftmark], A[rightmark] = A[rightmark], A[leftmark]


	A[rightmark],A[first] = A[first],A[rightmark]

	return rightmark

if __name__ == '__main__':
	A = map(int, sys.argv[1:])
	quick_sort(A)
	print A

			
