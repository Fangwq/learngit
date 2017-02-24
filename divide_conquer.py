# -*- coding: utf-8 -*-
import numpy as np

class divideConquer(object):
	def __init__(self, array):
		self._array = array

	# def minmax_main(self, array):   you can also use this method
	# 	n = len(array)
	# 	return self.minmax(0, n-1, array)
	
	def minmax(self, low, high, array):
		if high - low == 1:
			if array[low] < array[high]:
				return (array[low], array[high])
			else:
				return (array[high], array[low])
		else:
			mid = (low+high-1)/2
			x1, y1 = self.minmax(low, mid, array)
			x2, y2 = self.minmax(mid+1, high, array)
			x = min(x1, x2)
			y = max(y1, y2)
			return (x, y)

	def binarysearch(self, low, high, array, x):
		'''find element by using binary search'''
		if low >= high:
			return 'Do not find element'
		else:
			mid = (low+high-1)/2
			# print low, high
			if array[mid] == x:
				return mid
			elif x < array[mid]:
				return self.binarysearch(low, mid-1, array, x)
			else:
				return self.binarysearch(mid+1, high, array, x)

	def bottomup_merge(self, templist, p, q, r):
		'''merge method used by bottomup sort'''
		# templist = self._sortlist
		tempB = np.zeros(r-p+1)		#use this method,the memory used will be smaller.
		s = p-1; t = q; k = p-1
		while s <= q-1 and t <= r-1:
			if templist[s] <= templist[t]:
				tempB[k-(p-1)] = templist[s]
				s=s+1
			else:
				tempB[k-(p-1)] = templist[t]
				t=t+1
			k=k+1
		if s==q:
			for i in xrange(k, r):
				tempB[i-(p-1)] = templist[t]
				t=t+1
			# print "t={0}, r={1}".format(t,r),'===='
		else:
			for i in xrange(k, r):
				tempB[i-(p-1)] = templist[s]
				s=s+1
			# print "s={0}, q={1}".format(s,q),'####'
		for i in xrange(p-1,r):
			templist[i] = tempB[i-(p-1)]
		# print 'the auxiliary array:', tempB
		return templist[p-1:r]


	def mergesort(self, low, high, array):
		'''merge sort'''
		if low < high:
			mid = (low+high-1)/2
			self.mergesort(low, mid, array)
			# print array
			self.mergesort(mid+1, high, array)
			# print array
			self.bottomup_merge(array, low+1, mid+1, high+1)
		return array

	def select(self, low, high, array, index):
		'''find the indexth smallest element'''
		p = high - low +1
		if p < 44:
			array = self.mergesort(low, high, array)
			return array[index-1]
		else:
			q = (p-1)/5
			A = [[] for i in xrange(q)]
			for i in xrange(q):				
				A[i]=array[i*5:(i*5+5)]   #append every five elment into []
			M = []
			# print A[0]
			for i in xrange(q):
				self.mergesort(0, 4, A[i])
				M.append(A[i][2])
			mm = self.select(0, q-1, M, (q+1)/2)  
			A1 = []
			A2 = []
			A3 = []
			for i in xrange(p):
				if array[i] < mm:
					A1.append(array[i])
				elif array[i] == mm:
					A2.append(array[i])
				else:
					A2.append(array[i])
			if len(A1) > index:
				return self.select(0, len(A1)-1, A1, index)
			if len(A1) + len(A2) >= index:
				return mm
			if len(A1) + len(A2) < index:
				return self.select(0, len(A3)-1, A3, index-len(A1)-len(A2))









