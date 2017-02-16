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
		if i < self._length:
			# print i
			for j in xrange(i+1, self._length):
				print j,
				print ''
				if templist[j] < templist[i]:
					templist[j], templist[i] = templist[i], templist[j]
			self.rec_SelectSort(i+1)
		# print templist
		return templist