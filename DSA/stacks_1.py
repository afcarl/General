from collections import deque

class stacks(object):
	def __init__(self,stack_size):
		# initialize stack with size
		self.stack_size = stack_size
		self.d = deque(maxlen = self.stack_size)

	def pop(self):
		# check size of stack so that if it's - there is nothing to pop
		if len(self.d)==0:

			return 'error'
		else:

			return self.d.pop()
			#print self.d

	def push(self,value):
		# check if the stack has space to push value
		if self.isEmpty():
			self.d.append(value)
			#print self.d
			
		else:
			print "stack is full"
			

	def isEmpty(self):
		# is empty - there should be space for atleast one value 
		# else stack is full
		if len(self.d) < self.stack_size:
			return True

		else:
			return False

	def top(self):
		# return the top values
		if len(self.d) == 0:
			return "none"

		else:
			return self.d[-1]
			



if __name__ == '__main__':
	# Uncomment below line for just playing with stacks
	# s = stacks(4)
	# s.pop()
	# s.push(3)
	# s.push(1)
	# s.push(3)
	# s.push(2)
	# s.push(9)
	# s.top()
	# s.pop()

	# Reverse a string

	input_string = "priya"
	s = stacks(len(input_string))
	for i in input_string:
		s.push(i)
	reversed_string = []
	while(s.top()!="none"):
		
		reversed_string.append(s.pop())
		
	print ''.join(reversed_string)

