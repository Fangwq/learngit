# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
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
print b3_heap.delete(a3,6)
a4 = np.array([4,3,8,10,11,13,7,30,17,26])
b4_heap=structure_heap(a4)
print b4_heap.make_heap(a4)
count = 50
a5 = np.random.rand(count)*2.0-1.0 
b5_heap=structure_heap(a5)
b5_sample=b5_heap.heapsort(a5)
plt.figure()
plt.plot(xrange(count),b5_sample,'ro')
plt.show()


