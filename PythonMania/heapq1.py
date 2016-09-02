import heapq
# heap is used to get the nlargest or nsmallest elements in the list/dict
# deque is used to get/keep limited history of elements during iteration - collections.deque()	
# appending or removing elements from deque is O(1) complexity while doing the same on the list in O(n) 
ls = [1,2,3,3,1,2,3]
print heapq.nlargest(3,set(ls))
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


# Remember that a heap is formed - underneath using heapq - and heap[0] is always the smallest no.
# so if you pop the element from a "heaped list" - you pop the element once - the smallest comes out
# pop it again - the next smallest comes out

# >>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# >>> import heapq
# >>> heap = list(nums)
# >>> heapq.heapify(heap)
# >>> heap
# [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
# >>>
# The most important feature of a heap is that heap[0] is always the smallest item. Moreover, subsequent items can be easily found using the heapq.heappop() method, which pops off the first item and replaces it with the next smallest item (an operation that requires O(log N) operations where N is the size of the heap). For example, to find the three smallest items, you would do this:

# >>> heapq.heappop(heap)
# -4
# >>> heapq.heappop(heap)
# 1
# >>> heapq.heappop(heap)
# 2