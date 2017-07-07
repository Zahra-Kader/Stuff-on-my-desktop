# -*- coding: utf-8 -*-
"""
Created on Thu May 04 17:43:33 2017

@author: Zahra
"""
#Arrays allow you to print x squared. x=range() does not allow this because it returns type list
import numpy

x=numpy.arange(0,10)

print x**2

print 'type(x) is ' + repr(type(x))



x=range(0,10)

print 'type(x) is now ' + repr(type(x))

print x**2