# -*- coding: utf-8 -*-
import numpy as np
import copy

class closest_pair(object):
	def __init__(self, array):
		self.array = array
		# self.length = len(array)

	def distance(self, a, b):
		return np.square((a[0] - b[0])**2 + (a[1] - b[1])**2 )

	def cp(self, low, high, array):
		# temp = copy.copy(array)
		length = len(array)
		array.sort()       						#the array has to be list type: sort by x
		if high - low + 1 <= 3:
			L1 = self.distance(array[low], array[low + 1])
			L2 = self.distance(array[low], array[high])
			L3 = self.distance(array[low + 1], array[high])
			detal = min(L1, L2, L3)
		else:
			T = []
			mid = (low + high -1)/2
			x0 = array[mid][0]
			l_detal = self.cp(low, mid, array)
			r_detal = self.cp(mid+1, high, array)
			detal = min(l_detal, r_detal)
			k = 0
			array.sort(key=lambda x: x[1])   		#sort by y
			for i in xrange(length):
				if abs(array[i][0] - x0) <= detal:
					k = k + 1
					T.append(array[i])
			prime_detal = 2*detal
			for i in xrange(k-1):
				for j in xrange(i+1, min(i+7, k)):
					dis = self.distance(T[i], T[j])
					if dis < prime_detal:
						prime_detal = dis
						x = T[i]
						y = T[j]
						print x, y
			detal = min(detal, prime_detal)
		return detal

count = 10
alpha = np.random.rand(count)*10.0 - 5.0
beta = np.random.rand(count)*10.0 - 5.0
rand = []
for i in xrange(count):
	rand.append([alpha[i],beta[i]])
r = closest_pair(rand)
result = r.cp(0, count-1, rand)
print result