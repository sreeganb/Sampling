#!/usr/bin/env python3

import numpy as np
import pandas as pd

# generate a random number between -1 and 1 in both the x and y directions
# check if the number is within the circle or not
# If its inside circle count it as hit
m = 20000 # number of trials

def gen_rand():
    x1 = 2*np.random.random_sample() - 1
    y1 = 2*np.random.random_sample() - 1
    return x1,y1

x,y = gen_rand()
a = np.zeros(m)

for i in range(m):
    x, y=gen_rand()
    if x**2+y**2 < 1:
        a[i] = 1
    else:
        pass
print("number of hits:", np.sum(a))
print("value of pi is:", np.sum(a)/m*4)
