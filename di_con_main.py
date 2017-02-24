# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from divide_conquer import divideConquer
import copy

count = 2**8
a0 = np.random.rand(count)*2.0-1.0 
a2 = copy.copy(a0)
a3 = copy.copy(a0)
b0_method = divideConquer(a0)
b0_sample = b0_method.minmax(0,count-1, a0)
print b0_sample,min(a0),max(a0)
# ======================================
a1 = np.array([1, 4, 6, 9, 10 ])
b1_method = divideConquer(a1)
b1_sample = b1_method.binarysearch(0, len(a1)-1, a1, 12)
print b1_sample,
# ======================================
print 'before sort',a2
b2_method = divideConquer(a2)
b2_sample = b2_method.mergesort(0, count-1, a2)
print b2_sample
print 'original array:', a3
b3_method = divideConquer(a3)
b3_sample = b3_method.select(0, count-1, a3, 10)
print 'sorted array:',b3_method.mergesort(0, count-1, a3)
print b3_sample
plt.figure()
plt.plot(xrange(count),b2_sample,'ro')
plt.show()