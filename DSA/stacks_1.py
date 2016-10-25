from collections import deque

class stacks(object):
	def __init__(self,stack_size):
		self.stack_size = stack_size
		self.d = deque(maxlen = self.stack_size)

	def pop(self):
		
		if len(self.d)==0:
			print "no value to pop"
		else:

			self.d.pop()
			print self.d

	def push(self,value):
		if self.isEmpty():
			self.d.append(value)
			print self.d
			
		else:
			print "stack is full"
			

	def isEmpty(self):
		if len(self.d) < self.stack_size:
			return True

		else:
			return False

	def top(self):
		if len(self.d) == 0:
			print "no value to show"

		else:
			print self.d[-1]
			



if __name__ == '__main__':
	s = stacks(4)
	s.pop()
	s.push(3)
	s.push(1)
	s.push(3)
	s.push(2)
	s.push(9)
	s.top()
	s.pop()
