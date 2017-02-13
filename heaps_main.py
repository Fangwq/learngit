# -*- coding: utf-8 -*-
import numpy as np
from heaps import structure_heap

a0=np.array([20,17,9,10,11,4,5,3,7,25])
b0_heap=structure_heap(a0)
print b0_heap.siftup(a0,9)
a1=np.array([20,3,9,10,11,4,5,3,7,5])
b1_heap=structure_heap(a1)
print b0_heap.siftdown(a1,1)
a2=np.array([20,17,9,10,11,4,5,3,7,5])
b2_heap=structure_heap(a2)
print b2_heap.insert(a2,30)
a3=np.array([20,17,9,10,11,4,5,3,7,5])
b3_heap=structure_heap(a3)
print b3_heap.delete(a3,9)


