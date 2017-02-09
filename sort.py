# -*- coding: utf-8 -*-
import numpy as np

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
	def bubblesort(self, templist):
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

	def bottomup_merge(self, templist, p, q, r):
		templist = self.__sortlist
		tempB = np.zeros(self.__num)
		s = p-1; t = q; k = p-1
		while s <= q-1 and t <= r-1:
			if templist[s]<=templist[t]:
				tempB[k]=templist[s]
				s=s+1
			else:
				tempB[k]=templist[t]
				t=t+1
			k=k+1
		if s==q:
			for i in xrange(k, r):
				tempB[i]=templist[t]
				t=t+1
			# print t,r,'===='
		else:
			for i in xrange(k, r):
				tempB[i]=templist[s]
				s=s+1
			# print s,q,'####'
		for i in xrange(p-1,r):
			templist[i]=tempB[i]
		return templist[p-1:r]

	def bottomupsort(self,templist):
		templist = self.__sortlist
		t=1
		while t < self.__num:
			s=t; t=2*s; i=0
			while i+t < self.__num:
				self.bottomup_merge(templist, i+1, i+s, i+t)
				i=i+t
			if i+s < self.__num:
				self.bottomup_merge(templist, i+1, i+s, self.__num)
		return templist



