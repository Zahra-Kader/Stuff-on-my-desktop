# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:48:10 2017

@author: KaderF
"""
import numpy as np
from matplotlib import pyplot as plt

m=1024
a=-1.0
b=1.0
dt=m/(b-a)
t=np.linspace(a,b,m)
nu=np.fft.fftfreq(m)        #dimensionless freq
nu = np.fft.fftshift(nu)   # Shift zero freq to center
nu=nu*dt               #This gives freq in yr^-1

spacing=(b-a)/m

def powerspec(f):
    f=(np.fft.fft(f))/m   #Divide by the number of non zero terms
    f=np.fft.fftshift(f)    # Shift zero freq to center
    f_sq=np.absolute(f)**2 
    return f, f_sq

sig=0.1
y_gauss=np.exp(-0.5*(t-0)**2/(sig)**2) #white noise in time domain
y_gauss_ft,y_gauss_ps=powerspec(y_gauss),powerspec(y_gauss)
plt.subplot(4,1,1)
plt.plot(t,y_gauss)
plt.show()
plt.subplot(4,1,2)
plt.plot(nu,y_gauss_ft)
plt.show()

plt.subplot(4,1,3)
y_sin=np.sin(2*np.pi*t)
y_sin_noise=np.sin(2*np.pi*t)+np.random.randn()
y_sin_ft=powerspec(y_sin)
y_sin_noise_ft=powerspec(y_sin_noise)
#plt.plot(t_gauss,y_sin)
plt.plot(nu,y_sin_ft)
plt.show()

plt.subplot(4,1,4)
plt.plot(y_sin_noise_ft)
plt.show()

