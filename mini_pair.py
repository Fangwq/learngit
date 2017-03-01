# -*- coding: utf-8 -*-
import numpy as np
import copy
import matplotlib.pyplot as plt


class closest_pair(object):
	def __init__(self, array):
		self.array = array
		# self.length = len(array)

	def distance(self, a, b):
		return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 )

	def cp(self, low, high, x_array, y_array):
		# temp = copy.copy(array)
		length = len(x_array)
		if high - low + 1 <= 3:
			# print x_array,'======',low, high
			if high <= low:
				print 'what happens'
			if high - low + 1 ==2:
				detal = self.distance(x_array[low],x_array[high])
				xpoint = low
				ypoint = high
				# print low, high, detal, '====='
			else:
				L1 = self.distance(x_array[low], x_array[low + 1])
				L2 = self.distance(x_array[low], x_array[high])
				L3 = self.distance(x_array[low + 1], x_array[high])
				index = np.argmin([L1, L2, L3])
				if index == 0:
					xpoint = low
					ypoint = low + 1
				elif index == 1:
					xpoint = low
					ypoint = high
				else:
					xpoint = low + 1
					ypoint = high
				detal = min(L1, L2, L3)
				# print low, high, detal, '*****'
		else:
			T = []
			mid = (low + high -1)/2
			x0 = x_array[mid][0]
			l_detal = self.cp(low, mid, x_array, y_array)
			r_detal = self.cp(mid+1, high, x_array, y_array)
			detal = min(l_detal[0], r_detal[0])
			index = np.argmin([l_detal[0], r_detal[0]])
			if index == 0:
				xpoint = l_detal[1]
				ypoint = l_detal[2]
			else:
				xpoint = r_detal[1]
				ypoint = r_detal[2]
			k = 0
			# print y_array,'******'
			for i in xrange(length):
				if abs(y_array[i][0] - x0) <= detal:
					k = k + 1
					T.append(y_array[i])
			# print T,'######'
			prime_detal = 2*detal
			for i in xrange(k-1):
				for j in xrange(i+1, min(i+7, k)):
					dis = self.distance(T[i], T[j])
					if dis < prime_detal:
						prime_detal = dis
						temp_xpoint = i            #temp_xpoint is the index in y_array
						temp_ypoint = j
			detal = min(detal, prime_detal)
			index = np.argmin([detal, prime_detal])
			if index != 0:                         #find the index in x_array
				x = T[temp_xpoint]
				y = T[temp_ypoint]
				xpoint = x_array.index(x)
				ypoint = x_array.index(y)
			# print detal, '===='
		return detal, xpoint, ypoint

count = 10
alpha = np.random.rand(count)*10.0 - 5.0
beta = np.random.rand(count)*7.0 - 5.0
rand = []
for i in xrange(count):
	rand.append([alpha[i],beta[i]])
# print rand
rand.sort() 							#sort by x
X = rand
temp = copy.copy(X)
temp.sort(key=lambda x: x[1])   		#sort by y
Y = temp
# print X
# print Y
r = closest_pair(rand)
result = r.cp(0, count-1, X, Y)
one_pair = X[result[1]]
two_pair = X[result[2]]
print 'the closest distance and its index:',result
print 'the closest two point is:', one_pair, two_pair
print 'check the result:', r.distance(one_pair, two_pair)
X = np.transpose(X)
plt.figure()
plt.plot(X[0], X[1], 'ro')
plt.plot([one_pair[0], two_pair[0]], [one_pair[1], two_pair[1]], 'b-', lw=2)
plt.show()