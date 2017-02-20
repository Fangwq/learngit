# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

class recurrence_sort(object):
	def __init__(self, array):
		self._array = array
		# length = len(array)

	def rec_SelectSort(self, index):
		templist = self._array
		length = len(templist)
		i = index
		if i < length-1:
			# print range(i+1, length)
			for j in xrange(i+1, length):
				if templist[j] < templist[i]:
					templist[j], templist[i] = templist[i], templist[j]
			self.rec_SelectSort(i+1)
		# print templist
		return templist

	def rec_InsertSort(self, index):
		templist = self._array
		length = len(templist)
		i = index
		# if i > 1:      #two conditions with two different recursion form
		if i < length:
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
		piece = 10   #it shoule be larger than 9
		for j in xrange(digit):
			L = [[] for i in xrange(piece)]
			while len(array) > 0 :
				a = array[0]    
				# print a, array, '==='
				array.pop(0)
				k = a/10**j % 10
				L[k].append(a)
			array = L[0]
			for i in xrange(1,piece):
				array.append(L[i])
			array = [y for x in array for y in x]     #get the element in a list of list, just like flatten
			# print array
		return array

	def rec_exp(self, number, times):
		y = 1
		n = int(bin(times).replace('0b',''))   #get binary representation and change it to int number
		temp = [] 
		while n != 0:
			temp.append(n % 10)
			n = n/10
		k = len(temp)
		for i in xrange(k-1,-1,-1):
			y = y**2
			if temp[i]==1:
				y = number*y
		return y