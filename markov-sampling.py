#!/usr/bin/env python3

# Markov chain sampling to find the value of Pi

import numpy as np
import pandas as pd

delta = 0.4

def get_rand():
    x1 = 2*delta*np.random.random_sample() - delta
    y1 = 2*delta*np.random.random_sample() - delta
    return x1,y1
# Some initializations
nsamp = 8000
nhits = 0
x=1
y=1

for i in range(nsamp):
    x1, y1 = get_rand()
    if abs(x + x1) < 1 and abs(y + y1) < 1:
        x = x + x1
        y = y + y1
    else:
        pass
    if x**2+y**2 < 1:
        nhits = nhits + 1
    else:
        pass
  
print("number of hits:", nhits)
print("value of pi is:", nhits/nsamp*4)
