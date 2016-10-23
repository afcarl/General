class Node:

	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		#print self.cargo
		return (str(self.cargo)+" "+str(self.next))

	def test(self):
		print "testing"


if __name__ == '__main__':
	node1 = Node(1) 
	node2 = Node(2) 
	node3 = Node(3) 
	node1.next = node2
	node2.next = node3 
	print node1
	# a = 0
	# obj = []
	# for i in [1,2,3,4,5]:
	# 	node = "node"+str(a)
	# 	globals()[node] = Node(i)

	# 	obj.append(globals()[node])
	# 	#print globals()[node]
		
	# 	#globals()[node].test()
	# 	a = a+1
	# print node1

	# node1.next = node2
	# print node1,'last'

	# print obj
	
	# for i in range(len(obj)):
	# 	if i == len(obj)-1:
	# 		obj[i].next = 0
	# 		break
	# 	obj[i].next = obj[i+1]


	# print node1,'node2'

		
