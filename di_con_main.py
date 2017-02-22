# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from divide_conquer import divideConquer
# import copy

count = 2**5
a0 = np.random.rand(count)*2.0-1.0 
# a1 = copy.copy(a0)
b0_method = divideConquer(a0)
b0_sample = b0_method.minmax(0,count-1, a0)
print b0_sample,min(a0),max(a0)
a1 = np.array([1, 4, 6, 9, 10 ])
b1_method = divideConquer(a1)
b1_sample = b0_method.binarysearch(0, len(a1)-1, a1, 12)
print b1_sample