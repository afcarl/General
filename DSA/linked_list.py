class Node(object):
	def __init__(self,d,n=None):
		self.data = d
		self.next_node = n

	def get_next(self):
		return self.next_node


	def set_next(self,n):
		self.next_node = n

	def get_data(self):
		return self.data

	def set_data(self,d):
		self.data = d


class LinkedList(object):

	def __init__(self,r=None):
		self.root = r
		self.size = 0

	def get_size(self):
		return self.size

	def add(self,d):
		new_node = Node(d,self.root)
		self.root = new_node
		self.size+=1

	def add_position(self,d,n):
		if n==0:
			self.add(d)
		else:
			prev_node = None
			this_node = self.root
			p = 0
			while(p!=n):
				prev_node = this_node
				this_node = this_node.next_node

				p = p+1
			# replace now
			new_node = Node(d)
			prev_node.next_node = new_node
			new_node.next_node = this_node 



	def remove(self,d):
		#print self.root
		this_node = self.root
		prev_node = None

		while this_node:

			if this_node.get_data() == d:
				if prev_node:
					prev_node.set_next(this_node.next_node)

				else:
					self.root = this_node.get_next()

				self.size -=1
				return True



			else:
				prev_node = this_node
				this_node = this_node.next_node

		return False

	def find(self,d):
		this_node = self.root
		while this_node:
			if this_node.get_data() == d:
				return d

			else:
				this_node = this_node.get_next()

		return None



if __name__ == '__main__':
	myList = LinkedList(5)
	myList.add(5)
	myList.add(8)
	myList.add(12)
	print("size="+str(myList.get_size()))
	myList.remove(8)
	print("size="+str(myList.get_size()))
	myList.add_position(1,1)
	print(myList.remove(1))
	print("size="+str(myList.get_size()))
	print(myList.find(5))