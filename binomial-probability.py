#!/usr/bin/env python3

# Created on 06/17/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: demonstrate a binomial probability distribution of getting 2 heads from 10 coin flips
# Explanation: 
import numpy as np
from scipy import stats
import pylab as plt

n = 10
p = 0.3
k = np.arange(0,21)

binom = stats.binom.pmf(k, n, p)

plt.plot(k, binom, 'o-')

plt.show()