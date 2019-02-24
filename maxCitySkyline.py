#encoding:UTF-8
#author:justry

import os
import numpy as np

a = [[9, 4, 8, 7],
     [9, 4, 8, 7],
     [9, 4, 8, 7],
     [9, 4, 8, 7]]

b = [[8, 8, 8, 8],
     [7, 7, 7, 7],
     [9, 9, 9, 9],
     [3, 3, 3, 3]]

def func(i):
    return min(i)

c = np.apply_along_axis(func, -1, np.array([a, b]).transpose([1, 2, 0]))
print('end')