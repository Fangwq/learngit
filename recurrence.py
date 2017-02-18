# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from recurrenceSort import recurrence_sort
import copy
import sys
sys.setrecursionlimit(1500)    # set the maximum depth as 1500

count = 120
a0 = np.random.rand(count)*2.0-1.0 
a1 = copy.deepcopy(a0)  
print 'before sort:', a0
b0_method = recurrence_sort(a0)
b0_sample = b0_method.rec_SelectSort(0)
print 'after sort:', b0_sample
print 'before sort:', a1
b1_method = recurrence_sort(a1)
b1_sample = b1_method.rec_InsertSort(0)
print 'after sort:', b1_sample
a2=[7467,1247,3275,6792,9187,9134,4675,1239]
print 'before sort:', a2
b2_method = recurrence_sort(a2)
b2_sample = b1_method.radixsort(a2,4)
print 'after sort:', b2_sample
b3_method = recurrence_sort(64)
print b3_method.rec_exp(64,2)

plt.figure()
plt.plot(xrange(count), b0_sample, 'ro')
plt.plot(xrange(count), b1_sample, 'g+')
plt.xlim(-1, count+1)
plt.ylim(-1.05, 1.05)
plt.show()