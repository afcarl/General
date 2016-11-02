#!usr/bin/env/python27

import sys

def findElement(l,a):
	"""
	Binary tree search on a sorted array. Complexity is O(log(n))
	Inputs the sorted list, and the element to be found
	l and a respectively in this case.
	It returns the index of the element if it exists in the list else it returns -1
	
	"""
	start = 0 # intialize the start pointer for the sorted list to 0
	end = len(l) - 1 # initialize the end pointed for the sorted list to the last index

	while(start<=end):
		mid = (start+end)/2

		if l[mid]==a:
			return mid

		elif l[mid]<a:
			start = mid+1

		elif l[mid]>a:
			end = mid - 1


	return -1


	



if __name__ == '__main__':

	l = map(lambda x: int(x),sys.argv[1:]) # input the elements for the list as arguments
	l = sorted(l) # sort the array for binary search
	print l
	to_find = raw_input("Please enter the element you want to find: \n") # input the element you want to find in the list
	to_find = int(to_find)

	print findElement(l,to_find)







