# -*- coding: utf-8 -*-
import numpy as np

class dynamic_programming(object):
	def __init__(self, A):
		self.A = A
		# self.B = B

	def common_sequence(self, A, B):    #how to get the common sequence?
		n = len(A)
		m = len(B)
		L = np.array([[0]*(m+1) for i in xrange(n+1)])    #(n+1)*(m+1) array
		# print L
		for i in xrange(1, n+1):
			for j in xrange(1, m+1):
				if A[i-1] == B[j-1]:
					L[i, j] = L[i-1, j-1] + 1
					# print L
				else:
					L[i, j] = max(L[i, j-1], L[i-1, j])
		# print L
		return L[n-1, m-1]

	def matchain(self, R):
		length = len(R)-1
		C = np.array([[0]*(length) for i in xrange(length)])
		for d in xrange(length - 1):
			for i in xrange(length - d -1):
				j = i + d +1
				C[i, j] = 10**10
				for k in xrange(i+1, j+1):
					print C[i, j], C[i, k-1] + C[k, j] + R[i]*R[k]*R[j+1]
					C[i, j] = min(C[i, j], C[i, k-1] + C[k, j] + R[i]*R[k]*R[j+1])
		return C


