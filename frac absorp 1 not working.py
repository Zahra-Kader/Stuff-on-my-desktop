# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 03:04:23 2017

@author: Zahra
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:16:42 2017

@author: Zahra
"""

from sympy import Float,Number
import numpy as np
from matplotlib import pyplot as plt
from blandford import L31,L42,L44,L22,L33,L62,L64,L66,L51,L53,L55,L71,L73,L75,L77,L82,L84,L88,i_t2

m=4096
a=-16.0
b=16.0
dt=m/(b-a)
#def fz(N):
   # return dt*(b-(N/2))
#def sz(N):
   # return fz+N*dt
#def n1(N):
    #return dt*N
t=np.linspace(a,b,m)
nu=np.fft.fftfreq(m)        #dimensionless freq
nu = np.fft.fftshift(nu)   # Shift zero freq to center
nu= nu*dt              #This gives freq in yr^-1

L11=1.0
L86=0.4


def fitfunc(f,N):
    f[0:dt*(b-(N/2))]=0
    f[dt*(b-(N/2))+N*dt:4096]=0
    f=(np.fft.fft(f))/(dt*N)    #Divide by the number of non zero terms
    f=np.fft.fftshift(f)    # Shift zero freq to center
    f_sq=np.absolute(f)**2 
    return f_sq
    
def y1(w):
    y1=w*np.ones(m)
    return y1

def y2(t):
    y2=L22*t
    return y2
def y3(b,c):
    y3=b*1.0+c*t**2
    return fitfunc(y3)
def y8(d,e,f,g):
    y8=d*t+e*np.sin(2*np.pi*t)+f*np.cos(2*np.pi*t)+g*np.sin(4*np.pi*t)
    return fitfunc(y8)
def y4(h,i):
    y4=h*t+i*np.sin(2*np.pi*t)
    return fitfunc(y4)
def y5(j,k,l):
    y5=j*1.0+k*t**2+l*np.cos(2*np.pi*t)
    return fitfunc(y5)
def y6(m,o,p):
    y6=m*t+o*np.sin(2*np.pi*t)+p*t*np.cos(2*np.pi*t)
    return fitfunc(y6)
def y7(q,r,s,u):
    y7=(q*1.0)+r*(t**2)+s*np.cos(2*np.pi*t)+u*t*np.sin(2*np.pi*t)
    return fitfunc(y7)

plt.subplot(3,1,1)
#plt.plot(nu,fitfunc(L11*np.ones(m),3), 'r',label='1')
plt.plot(nu,fitfunc(y2,3), 'g',label='2')
plt.xlim(0,4)

#plt.plot(nu,y3(L31,L33), 'b',label='3')
plt.plot(nu,fitfunc(L31*1.0+L33*i_t2,3), 'b',label='3')

plt.plot(nu,y8(L82,L84,L86,L88), 'm',label='8')
plt.xlim(0,4)
plt.xlabel('Frequency f (yr^-1)')
plt.ylabel('Fractional absorption')
plt.legend(loc='upper right')
plt.subplot(3,1,2)
plt.plot(nu,y4(L42,L44), 'r',label='4')
plt.plot(nu,y5(L51,L53,L55), 'g',label='5')
plt.plot(nu,y6(L62,L64,L66), 'b',label='6')
plt.plot(nu,y7(L71,L73,L75,L77), 'm',label='7')

plt.xlabel('Frequency f (yr^-1)')
plt.ylabel('Fractional absorption')
plt.legend(loc='upper right')
plt.ylim(0,1)
plt.xlim(0,4)
plt.show()

fitfunc_sum=y1(L11)+y2(L22)+y3(L31,L33)+y4(L42,L44)+y5(L51,L53,L55)+y6(L62,L64,L66)+y7(L71,L73,L75,L77)+y8(L82,L84,L86,L88)
T=1.0-(fitfunc_sum)
    
plt.subplot(3,1,3)  
plt.plot(nu,T)
plt.xlim(0,7)
plt.ylim(0,1)
plt.show()