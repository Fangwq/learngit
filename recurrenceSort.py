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

	def permutation(self, index, array):   		#the code here is wrong
		num = len(array)
		if index == num:
			return array
		else:
			# print array
			for i in xrange(index, num):
				array[i], array[index] = array[index],array[i]
				self.permutation(index+1,array)
				array[i], array[index] = array[index],array[i]
				# print array, '******'
		return array	

	def candidate(self, index, array):   
		i = index
		c = array[index]
		count = 1
		n = len(array)
		# print i, n
		while i < n-1 and count > 0:
			i = i+1 
			if array[i] == c: 
				count = count + 1
			else:
				count = count - 1
		# print i
		if i == n-1:
			return c
		else:
			return self.candidate(i+1, array)

	def majority(self, array):
		c = self.candidate(0, array)
		n = len(array)
		count = 0
		for j in xrange(n):
			if array[j] == c:
				count = count + 1
		if count > (n-1)/2:
			return c 
		else:
			return 'It does not have majority element'




