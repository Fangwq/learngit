# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from divide_conquer import divideConquer
import copy

count = 2**7
a0 = np.random.rand(count)*2.0-1.0 
a2 = copy.copy(a0)
a3 = copy.copy(a0)
a4 = copy.copy(a0)
b0_method = divideConquer(a0)
b0_sample = b0_method.minmax(0,count-1, a0)
print b0_sample,min(a0),max(a0)
# ======================================
a1 = np.array([1, 4, 6, 9, 10 ])
b1_method = divideConquer(a1)
b1_sample = b1_method.binarysearch(0, len(a1)-1, a1, 12)
print b1_sample
# ======================================
print 'before sort',a2
b2_method = divideConquer(a2)
b2_sample = b2_method.mergesort(0, count-1, a2)
print b2_sample
#=======================================
# print 'original array:', a3
merge_start = time.time()
b3_method = divideConquer(a3)
b3_sample = b3_method.mergesort(0, count-1, a3)
merge_end = time.time()
index = 10
b3_index = b3_method.select(0, count-1, a3, index)
print 'sorted array with mergesort:',b3_sample
print 'merge time:', "{:.5f}s".format(merge_end - merge_start)
print 'the {:}th smallest element: {:.10f}'.format(index, b3_index)
#=======================================
quick_start = time.time()
b4_method = divideConquer(a4)
b4_sample = b4_method.quicksort(0, count-1, a4)
quick_end = time.time()
# print 'sorted array with quicksort:',b4_sample
print 'quick time:', "{:.5f}s".format(quick_end - quick_start)

plt.figure()
plt.plot(xrange(count),b2_sample,'ro')
plt.plot(xrange(count),b3_sample,'b+')
plt.plot(xrange(count),b4_sample,'gd')
plt.show()