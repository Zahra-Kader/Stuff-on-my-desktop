# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:16:42 2017

@author: Zahra
"""

from sympy import Float,Number
import numpy as np
from matplotlib import pyplot as plt
from blandford import L31,L42,L44,L22,L33,L62,L64,L66,L51,L53,L55,L71,L73,L75,L77,L82,L84,L88
from blandfordN1 import L311,L421,L441,L221,L331,L621,L641,L661,L511,L531,L551,L711,L731,L751,L771,L821,L841,L881
from blandfordNt import L31t,L42t,L44t,L22t,L33t,L62t,L64t,L66t,L51t,L53t,L55t,L71t,L73t,L75t,L77t,L82t,L84t,L88t

Nt=10.0
N3=3.0
N1=1.0
m=4096
a=-16.0
b=16.0
dt=m/(b-a)
fz3=dt*(b-(N3/2))
fz3=np.int(fz3)
sz3=fz3+N3*dt
sz3=np.int(sz3)
n13=dt*N3
fz1=dt*(b-(N1/2))
fz1=np.int(fz1)
sz1=fz1+N1*dt
sz1=np.int(sz1)
n11=dt*N1
n13=dt*N3
fzt=dt*(b-(Nt/2))
fzt=np.int(fzt)
szt=fzt+Nt*dt
szt=np.int(szt)
n1t=dt*Nt

t=np.linspace(a,b,m)
nu=np.fft.fftfreq(m)        #dimensionless freq
nu = np.fft.fftshift(nu)   # Shift zero freq to center
nu=nu*dt               #This gives freq in yr^-1
              #This gives freq in yr^-1

L11=1.0
L86=0.4
L861=0.8
L86t=0.4


def fitfunc3(f):
    f[0:fz3]=0
    f[sz3:4096]=0
    f=(np.fft.fft(f))/n13    #Divide by the number of non zero terms
    f=np.fft.fftshift(f)    # Shift zero freq to center
    f_sq=np.absolute(f)**2 
    return f_sq

def fitfunc1(f):
    f[0:fz1]=0
    f[sz1:4096]=0
    f=(np.fft.fft(f))/n11   #Divide by the number of non zero terms
    f=np.fft.fftshift(f)    # Shift zero freq to center
    f_sq=np.absolute(f)**2 
    return f_sq

def fitfunct(f):
    f[0:fzt]=0
    f[szt:4096]=0
    f=(np.fft.fft(f))/n1t  #Divide by the number of non zero terms
    f=np.fft.fftshift(f)    # Shift zero freq to center
    f_sq=np.absolute(f)**2 
    return f_sq
    
def y1(w):
    y1=w*np.ones(m)
    return fitfunc3(y1)
def y2(a):
    y2=a*t
    return fitfunc3(y2)
def y3(b,c):
    y3=b*1.0+c*t**2
    return fitfunc3(y3)
def y8(d,e,f,g):
    y8=d*t+e*np.sin(2*np.pi*t)+f*np.cos(2*np.pi*t)+g*np.sin(4*np.pi*t)
    return fitfunc3(y8)
def y4(h,i):
    y4=h*t+i*np.sin(2*np.pi*t)
    return fitfunc3(y4)
def y5(j,k,l):
    y5=j*1.0+k*t**2+l*np.cos(2*np.pi*t)
    return fitfunc3(y5)
def y6(m,o,p):
    y6=m*t+o*np.sin(2*np.pi*t)+p*t*np.cos(2*np.pi*t)
    return fitfunc3(y6)
def y7(q,r,s,u):
    y7=(q*1.0)+r*(t**2)+s*np.cos(2*np.pi*t)+u*t*np.sin(2*np.pi*t)
    return fitfunc3(y7)

def y11(w):
    y11=w*np.ones(m)
    return fitfunc1(y11)
def y21(a):
    y21=a*t
    return fitfunc1(y21)
def y31(b,c):
    y31=b*1.0+c*t**2
    return fitfunc1(y31)
def y81(d,e,f,g):
    y81=d*t+e*np.sin(2*np.pi*t)+f*np.cos(2*np.pi*t)+g*np.sin(4*np.pi*t)
    return fitfunc1(y81)
def y41(h,i):
    y41=h*t+i*np.sin(2*np.pi*t)
    return fitfunc1(y41)
def y51(j,k,l):
    y51=j*1.0+k*t**2+l*np.cos(2*np.pi*t)
    return fitfunc1(y51)
def y61(m,o,p):
    y61=m*t+o*np.sin(2*np.pi*t)+p*t*np.cos(2*np.pi*t)
    return fitfunc1(y61)
def y71(q,r,s,u):
    y71=(q*1.0)+r*(t**2)+s*np.cos(2*np.pi*t)+u*t*np.sin(2*np.pi*t)
    return fitfunc1(y71)

def y1t(w):
    y1t=w*np.ones(m)
    return fitfunct(y1t)
def y2t(a):
    y2t=a*t
    return fitfunct(y2t)
def y3t(b,c):
    y3t=b*1.0+c*t**2
    return fitfunct(y3t)
def y8t(d,e,f,g):
    y8t=d*t+e*np.sin(2*np.pi*t)+f*np.cos(2*np.pi*t)+g*np.sin(4*np.pi*t)
    return fitfunct(y8t)
def y4t(h,i):
    y4t=h*t+i*np.sin(2*np.pi*t)
    return fitfunct(y4t)
def y5t(j,k,l):
    y5t=j*1.0+k*t**2+l*np.cos(2*np.pi*t)
    return fitfunct(y5t)
def y6t(m,o,p):
    y6t=m*t+o*np.sin(2*np.pi*t)+p*t*np.cos(2*np.pi*t)
    return fitfunct(y6t)
def y7t(q,r,s,u):
    y7t=(q*1.0)+r*(t**2)+s*np.cos(2*np.pi*t)+u*t*np.sin(2*np.pi*t)
    return fitfunct(y7t)

plt.subplot(3,1,1)
plt.plot(nu,y1(L11), 'r',label='1')
plt.plot(nu,y2(L22), 'g',label='2')
plt.plot(nu,y3(L31,L33), 'b',label='3')
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
plt.subplot(4,1,3)
plt.plot(nu,y1t(L11), 'r',label='1')
plt.plot(nu,y2t(L22t), 'g',label='2')
plt.plot(nu,y3t(L31t,L33t), 'b',label='3')
plt.plot(nu,y8t(L82t,L84t,L86t,L88t), 'm',label='8t')
plt.xlim(0,4)

fitfunc3_sum=y1(L11)+y2(L22)+y3(L31,L33)+y4(L42,L44)+y5(L51,L53,L55)+y6(L62,L64,L66)+y7(L71,L73,L75,L77)+y8(L82,L84,L86,L88)
T3=1.0-(fitfunc3_sum)

fitfunc1_sum=y11(L11)+y21(L221)+y31(L311,L331)+y41(L421,L441)+y51(L511,L531,L551)+y61(L621,L641,L661)+y71(L711,L731,L751,L771)+y81(L821,L841,L861,L881)
T1=1.0-(fitfunc1_sum)

fitfunct_sum=y1t(L11)+y2t(L22t)+y3t(L31t,L33t)+y4t(L42t,L44t)+y5t(L51t,L53t,L55t)+y6t(L62t,L64t,L66t)+y7t(L71t,L73t,L75t,L77t)+y8(L82,L84,L86,L88)
Tt=1.0-(fitfunct_sum)

plt.subplot(3,1,3)
plt.plot(nu,T3)
plt.plot(nu-0.6,T1)
plt.plot(nu,Tt)

plt.xlim(0,7)
plt.ylim(0,1)
plt.show()