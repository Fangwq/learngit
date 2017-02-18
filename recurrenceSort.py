# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

class recurrence_sort(object):
	def __init__(self, array):
		self._array = array
		self._length = len(array)

	def rec_SelectSort(self, index):
		templist = self._array
		i = index
		if i < self._length-1:
			# print range(i+1, self._length)
			for j in xrange(i+1, self._length):
				if templist[j] < templist[i]:
					templist[j], templist[i] = templist[i], templist[j]
			self.rec_SelectSort(i+1)
		# print templist
		return templist

	def rec_InsertSort(self, index):
		templist = self._array
		i = index
		# if i > 1:      #two conditions with two different recursion form
		if i < self._length:
			x = templist[i]
			# self.rec_InsertSort(i-1)
			j = i-1
			while j >= 0 and templist[j] > x:
				templist[j+1] = templist[j]
				j = j-1
			templist[j+1] = x
			self.rec_InsertSort(i+1)
		return templist

	def radixsort(self, array, digit):
		for j in xrange(digit):
			L = [[] for i in xrange(10)]
			while len(array) > 0 :
				a = array[0]    
				# print a, array, '==='
				array.pop(0)
				k = a/10**j % 10
				L[k].append(a)
			array = L[0]
			for i in xrange(1,10):
				array.append(L[i])
			array = [y for x in array for y in x]     #get the element in a list of list, just like flatten
			# print array
		return array

