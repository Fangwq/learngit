# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from recurrenceSort import recurrence_sort

count = 10
a0 = np.random.rand(count)*2.0-1.0 
print a0
b0_method = recurrence_sort(a0)
b0_sample = b0_method.rec_SelectSort(0)
plt.figure()
plt.plot(xrange(count),b0_sample,'ro')
plt.show()