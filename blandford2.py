# -*- coding: utf-8 -*-
"""
Created on Sun Jul 09 18:43:49 2017

@author: Zahra
"""

from scipy.integrate import quad
import math

N=3.0
t0=-N/2
t1=N/2
def f(t):
    return t**2

ans, err=quad(f,t0,t1)
print ans