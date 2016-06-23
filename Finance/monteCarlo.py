# -*- coding: utf-8 -*-
'''
MonteCarlo Simulation
'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
# Linear Congruential Generators for seeding
# zi+1=(azi+c)modmzi+1=(azi+c)modm 

# Hull-Dobell Theorem: The LCG will have a full period for all seeds if and onlh if

# cc and mm are relatively prime,
# a−1a−1 is divisible by all prime factors of mm
# a−1a−1 is a multiple of 4 if mm is a multiple of 4.

def rng(m=2**32, a=1103515245, c=12345):
	rng.current = (a*rng.current + c) % m
	return rng.current/m


rng.current = 1.0

# print [rng() for i in range(10)]

x = np.linspace(0, 1, 100)
plt.plot(x, np.exp(x));
pts = np.random.uniform(0,1,(100, 2))
pts[:, 1] *= np.e
plt.scatter(pts[:, 0], pts[:, 1])
plt.xlim([0,1])
plt.ylim([0, np.e])
#plt.show()
# Check analytic solution

from sympy import symbols, integrate, exp

x = symbols('x')
expr = integrate(exp(x), (x,0,1))
print expr.evalf()
# Using numerical quadrature
# You may recall elementary versions such as the
# trapezoidal and Simpson's rules
# Note that nuerical quadrature needs $n^p$ grid points
# in $p$ dimensions to maintain the same accuracy
# This is known as the curse of dimensionality and explains
# why quadrature is not used for high-dimensional integration

from scipy import integrate
integrate.quad(exp, 0, 1)
# Monte Carlo approximation

for n in 10**np.array([2]):#,2,3,4,5,6,7,8]):
    pts = np.random.uniform(0, 1, (n, 2))
    #print pts
    pts[:, 1] *= np.e
    #print pts
    count = np.sum(pts[:, 1] < np.exp(pts[:, 0]))
    print count
    volume = np.e * 1 # volume of region
    
    sol = (volume * count)/n
    print '%10d %.6f' % (n, sol)