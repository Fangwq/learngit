# -*- coding: utf-8 -*-
import numpy as np
from dynamic_program import dynamic_programming

stringA = 'xyxxzxyzxy'
stringB = 'zxzyyzxxyxxz'
a = dynamic_programming(stringA, stringB)
r = a.common_sequence(stringA, stringB)
print r