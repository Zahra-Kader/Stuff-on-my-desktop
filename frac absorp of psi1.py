# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:16:42 2017

@author: Zahra
"""

from sympy import Float,Number
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
from blandford import L31,L42,L44,L22,L33,L62,L64,L66,L51,L53,L55,L71,L73,L75,L77,L82,L84,L88

N=3.0
m=4096
a=-16.0
b=16.0
dt=m/(b-a)
fz=dt*(b-(N/2))
fz=np.int(fz)
sz=fz+N*dt
sz=np.int(sz)
n1=dt*N
t=np.linspace(a,b,m)
nu=np.fft.fftfreq(m)        #dimensionless freq
nu = np.fft.fftshift(nu)   # Shift zero freq to center
nu=nu*n1/N               #This gives freq in yr^-1
print len(nu)
nu_hertz=nu/(3.1536e7)
L11=1.0
L86=0.4


def fitfunc(f):
    f[0:fz]=0
    f[sz:4096]=0
    f=(np.fft.fft(f))/n1    #Divide by the number of non zero terms
    f=np.fft.fftshift(f)    # Shift zero freq to center
    f_sq=np.absolute(f)**2 
    return f_sq
    
def y1(w):
    y1=w*np.ones(m)
    return fitfunc(y1)
def y2(a):
    y2=a*t
    return fitfunc(y2)
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

#plt.subplot(3,1,1)
#plt.plot(nu,y1(L11), 'r',label='1')
#plt.plot(nu,y2(L22), 'g',label='2')
#plt.plot(nu,y3(L31,L33), 'b',label='3')
#plt.plot(nu,y8(L82,L84,L86,L88), 'm',label='8')
#plt.xlim(0,4)
#plt.xlabel('Frequency f (yr^-1)')
#plt.ylabel('Fractional absorption')
#plt.legend(loc='upper right')
#plt.subplot(3,1,2)
#plt.plot(nu,y4(L42,L44), 'r',label='4')
#plt.plot(nu,y5(L51,L53,L55), 'g',label='5')
#plt.plot(nu,y6(L62,L64,L66), 'b',label='6')
#plt.plot(nu,y7(L71,L73,L75,L77), 'm',label='7')

#plt.xlabel('Frequency f (yr^-1)')
#plt.ylabel('Fractional absorption')
#plt.legend(loc='upper right')
#plt.ylim(0,1)
#plt.xlim(0,4)
#plt.show()

fitfunc_sum=y1(L11)+y2(L22)+y3(L31,L33)+y4(L42,L44)+y5(L51,L53,L55)+y6(L62,L64,L66)+y7(L71,L73,L75,L77)+y8(L82,L84,L86,L88)
T=1.0-(fitfunc_sum)
P=nu**(-5)

def f(x):
    #if (np.abs(x)<1e-10):
       # res = T
    #else:
        #res = T*x**(-5)
    f=1.0-((x)**2)
    return f

#plot(X,f(X))
x=np.arange(-1.0,1.0,0.1)
def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        y,err = integrate.quad(f,0,val)
        res[i]=y
    return res

nu_new=np.linspace(0,5.0,m)
#plt.plot(nu,F(nu))
    
    
#plt.subplot(3,1,3)  
#plt.plot(nu_hertz,T)
#plt.plot(nu,P)
plt.plot(nu_new,T)
#plt.plot(nu,P*T)
#plt.plot(nu,1.0/T)
#plt.plot(nu,P)
#plt.xlim(0,0.0000005)
plt.xlim(2,3)
plt.ylim(0,1)
plt.show()