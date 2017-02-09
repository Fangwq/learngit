# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

class algorithm_sort(object):
	'''Usage: sort a list

	input: 
		a random unsorted array

	return:
		a sorted array
	'''
	def __init__(self,sortlist):
		self.__sortlist = sortlist		#private variable

	# @staticmethod @classmethod		
	def bubbleSort(self,templist):
		templist=self.__sortlist
		i = 0
		num = len(templist)
		args = False
		while i <= num-1 and not args:
			args = True
			for j in xrange(num-1,i,-1):
				if templist[j] < templist[j-1]:
					templist[j], templist[j-1] = templist[j-1], templist[j]		#interchange j and j-1
					args = False
			i = i+1
			# print templist, args
		return templist

count = 500
a = np.random.rand(count)*2.0-1.0 
print 'before sorted:', a
method = algorithm_sort(a)
b = method.bubbleSort(a)
print 'after sorted:', b
k = np.random.randint(count)
print k
sample=b[0:k]
plt.figure()
plt.plot(xrange(k),sample,'ro')
plt.show()
