# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
a=-5
b=5
m=100
x=np.linspace(a,b,m)
xft=np.fft.fftfreq(m)
xft=np.fft.fftshift(x)
xft=xft*(m/(b-a)) #to get it in frequencies of Hertz, multiply by df*N where df=1/T and T is range b-a and N is number of points m. 
y=np.sin(2*np.pi*x)
yft=np.fft.fft(y)/m
yft=np.fft.fftshift(yft)
yft=yft**2
#plt.plot(x,y)
plt.plot(xft,yft)