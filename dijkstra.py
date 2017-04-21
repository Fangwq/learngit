# -*- coding: utf-8 -*-
import numpy as np

n = 6
v = set([i for i in xrange(n)])
length = np.array([[float("inf"), 1, 12, float("inf"),float("inf"),float("inf")],
                  [1, float("inf"), 9, 3, float("inf"),float("inf")], 
                  [12, 9, float("inf"), 4, 5, float("inf")], 
                  [float("inf"), 3, 4, float("inf"), 13, 15],
                  [float("inf"), float("inf"), 5, 13, float("inf"), 4], 
                  [float("inf"), float("inf"), float("inf"), 15, 4, float("inf")]])
lamda = np.array([0]*n) 
X = set([0])
Y = v - X
#print type(X)
#print X, Y, np.shape(length), type(length)
index = [0]
k = 0
for i in xrange(1, n-1):
    temp = np.amin(length[k, :])    #get the minimum value in an array
    index.append(np.argmin(length[k, :]))
    lamda[i] = temp + lamda[i-1]
    X.add(index[-1])
    Y = Y - {index[-1]}
    for j in Y:
        print j, Y
        if length[k, j] != float("inf") and length[index[-1], j] != float("inf") and temp + length[index[-1], j] < length[k, j]:
            lamda[i+1] = temp + length[index[-1], j]
            k = j
        elif length[k, j] != float("inf") and length[index[-1], j] != float("int") and temp + length[index[-1], j] > length[k, j]:
            lamda[i+1] = length[k, j]
            k = j
print lamda, index
            


