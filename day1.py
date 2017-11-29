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

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = 10 + np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

plt.subplot(2, 1, 1)
plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.subplot(2, 1, 2)
plt.plot(xf[1:], 2.0/N * np.abs(yf[0:N/2])[1:])

import numpy as np
import matplotlib.pyplot as plt

N=600
T=1.0 / 800.0
a=-N*T/2
b=N*T/2
x=np.arange(-N*T/2,N*T/2,N)
xft=np.fft.fftfreq(N)
xft=np.fft.fftshift(x)
xft=xft*(N/(b-a))
y = 10 + np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yft=np.fft.fft(y)/N
yft=np.fft.fftshift(yft)
plt.plot(xft,yft)