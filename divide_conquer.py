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




