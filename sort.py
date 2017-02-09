# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import time

class algorithm_sort(object):
	'''Usage: sort a list

	input: 
		a random unsorted array

	return:
		a sorted array
	'''
	def __init__(self, sortlist):
		self.__sortlist = sortlist		#private variable
		self.__num = len(sortlist)
	# @staticmethod @classmethod		
	def bubbleSort(self, templist):
		templist=self.__sortlist
		i = 0
		args = False
		while i <= self.__num-1 and not args:
			args = True
			for j in xrange(self.__num-1, i, -1):
				if templist[j] < templist[j-1]:
					templist[j], templist[j-1] = templist[j-1], templist[j]		#interchange j and j-1
					args = False
			i = i+1
			# print templist, args
		return templist

	def selectsort(self,templist):
		templist = self.__sortlist
		for i in xrange(self.__num-1):
			k = i
			for j in xrange(i+1, self.__num):
				if templist[j] < templist[k]:
					k = j
			if k != i:
				templist[i], templist[k] = templist[k], templist[i]		#interchange i and k
		return templist

	def insertsort(self,templist):
		templist = self.__sortlist
		for i in xrange(1, self.__num):
			x = templist[i]
			j = i-1
			while j >= 0 and templist[j] > x:
				templist[j+1] = templist[j]
				j = j-1
			templist[j+1] = x
		return templist

count = 500
a = np.random.rand(count)*2.0-1.0 
print 'before sorted:', a
bubble_method = algorithm_sort(a)
select_method = algorithm_sort(a)
insert_method = algorithm_sort(a)
#===calculate the time consuming===
bubble_start = time.time()
b_bubble = bubble_method.bubbleSort(a)
bubble_end = time.time()
select_start = time.time()
b_select = select_method.selectsort(a)
select_end = time.time()
insert_start = time.time()
b_insert = insert_method.bubbleSort(a)
insert_end = time.time()
print 'bubble time:', "{:.5f}".format(bubble_end - bubble_start)
print 'select time:', "{:.5f}".format(select_end - select_start)
print 'insert time:', "{:.5f}".format(insert_end - insert_start)
# print 'after bubblesorted:', b_bubble
# print 'after selectsorted:', b_select
# print 'after insertsorted:', b_insert
k = np.random.randint(count)
print k
sample_bubble = b_bubble[0:k]
sample_select = b_select[0:k]
sample_insert = b_insert[0:k]
plt.figure()
plt.plot(xrange(k),sample_bubble,'ro')
plt.plot(xrange(k),sample_select,'b*')
plt.plot(xrange(k),sample_insert,'g+')
plt.show()
