# -*- coding: utf-8 -*-
import numpy as np

class dynamic_programming(object):
	def __init__(self, A, B):
		self.A = A
		self.B = B

	def common_sequence(self, A, B):
		n = len(A)
		m = len(B)
		L = np.array([[0]*(m+1) for i in xrange(n+1)])    #(n+1)*(m+1) array
		# print L
		for i in xrange(1, n+1):
			for j in xrange(1, m+1):
				if A[i-1] == B[j-1]:
					L[i, j] = L[i-1, j-1] + 1
					print L
				else:
					L[i, j] = max(L[i, j-1], L[i-1, j])
		print L
		return L[n-1, m-1]
