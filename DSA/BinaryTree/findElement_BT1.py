#!usr/bin/env/python27

import sys

def findElement(user_list,a):
	"""
	Binary tree search on a sorted array. Complexity is O(log(n))
	Inputs the sorted list, and the element to be found
	l and a respectively in this case.
	It returns the index of the element if it exists in the list else it returns -1
	
	"""
	start = 0 # intialize the start pointer for the sorted list to 0
	end = len(user_list) - 1 # initialize the end pointed for the sorted list to the last index

	while(start<=end): # only if start is before the end pointer
		mid = (start+end)/2

		if user_list[mid]==a:
			return mid # return the element if it is equal to the middle element of the considered part of the user_list

		elif user_list[mid]<a: 
			# move in the upper half of the user list to check for 
			# element and remove the lower half from further consideration by changing the start pointer value
			start = mid+1

		elif user_list[mid]>a:
			# move in the lower half of the user list to check for 
			# element and remove the upper half from further consideration by changing the end pointer value
			end = mid - 1


	return -1


	



if __name__ == '__main__':

	user_list = sorted(map(lambda x: int(x),sys.argv[1:])) # input the elements for the list as commandline arguments and sort it
	print user_list
	to_find = int(raw_input("Please enter the element you want to find: \n")) # input the element you want to find in the list
	print findElement(user_list,to_find)







