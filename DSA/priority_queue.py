


import heapq


class priority_queue():

	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self,item,priority):
		heapq.heappush(self._queue,(-priority,self._index,item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]


if __name__ == '__main__':
	

	q = priority_queue()
	q.push("priya",1)
	q.push("adi",2)
	q.push("nkd",3)
	q.push("pp",100)
	q.push("presh",101)
	print q.pop()