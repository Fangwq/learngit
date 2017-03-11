# -*- coding: utf-8 -*-
import numpy as np
from dynamic_program import dynamic_programming

stringA = 'xyxxzxyzxy'
stringB = 'zxzyyzxxyxxz'
a = dynamic_programming(stringA)
r = a.common_sequence(stringA, stringB)
print r
M = [5,10,4,6,10,2]
b = dynamic_programming(M)
result = b.matchain(M)
print result
l = np.array([[0, 2, 9],[8, 0, 6],[1, float("inf"), 0]])   #expression of Infinite
c = dynamic_programming(l)
d = c.floyd(l)
print d