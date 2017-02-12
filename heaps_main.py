# -*- coding: utf-8 -*-
import numpy as np
from heaps import structure_heap

a=np.array([20,17,9,10,11,4,5,3,7,25])
b_heap=structure_heap(a,9)
print b_heap.siftup(a,9)
