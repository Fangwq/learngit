# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from divide_conquer import divideConquer

count = 2**5
a0 = np.random.rand(count)*2.0-1.0 
b0_method = divideConquer(a0)
b0_sample = b0_method.minmax(0,count-1, a0)
print b0_sample,min(a0),max(a0)