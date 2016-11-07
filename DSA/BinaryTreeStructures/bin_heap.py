#!usr/bin/env/python2

import os
import sys

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percUp(self,i):
		while i//2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
				self.heapList[i],self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
			i = i//2

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percDown(self,i):
		while (i*2)<= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]

			i = mc

	def minChild(self,i):
		if i*2 + 1 > self.currentSize:
			return i*2
		else:
			if self.heapList[i*2] < self.heapList[i*2 + 1]:
				return i*2
			else:
				return i*2+1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,A):
		i = len(A)//2
		self.currentSize = len(A)
		self.heapList = [0] + A[:]
		while i>0:
			self.percDown(i)
			i = i-1
		print self.heapList


if __name__ == '__main__':
	B = BinHeap()
	B.buildHeap([1,4,0,3,2])