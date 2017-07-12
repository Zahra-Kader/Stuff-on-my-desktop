# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 22:45:48 2017

@author: Zahra
"""
from scipy.integrate import quad
import math
import numpy as np
import matplotlib.pyplot as plt

N=3.0                   #Number of years measurements are taken
t0=-N/2                 #lower integral limit
t1=N/2                  #upper integral limit
n=365.0                 #number of measurements taken each year
J=np.complex(0,1)
#p1=L11
#p2=L22*t
#p3=L31+L33*t**2

def integral(x):        #define the sum from i=1 to nN of the function x which can be approximated to n times the integral from -N/2 to N/2 
    ans,err=quad(x,t0,t1)
    return np.array(n*ans)
 
#For p1:
   
def int0(t):            #define the function t**0
    return t**0

print integral(int0)    #get the integral of  int0 using defined function in line 21-23

#n*integral of p1**2=1 so L11**2*n*(integral of dt from -1.5 to 1.5)=1 so (L11**2)*int0=1
L11=math.sqrt(1/(integral(int0)))
print L11,'b'

def p1(t):
    return L11*int0(t)
    
print integral(p1)

#Now we want to plot p1(f)=integral from -N/2 to N/2 of p1(t)*e**2pi*i*f*t,called p1n below, times the integral from -N/2 to N/2 of p1(t)*e**-2pi*i*f*t,called p1nc below, against f
mn=np.array([])             
f=np.linspace(0,4.0,100)    #create an array of f values 
for i in f:                 #find the integrals for each f value
    def p1n(t):
        return p1(t)*np.exp(2*J*np.pi*f*t)
    p1nin=(1/n)*integral(p1n)               #integral of p1n
    print p1nin
    def p1nc(t):
        return p1(t)*np.exp(-2*J*np.pi*f*t)    
    p1ncin=(1/n)*integral(p1nc)             #integral of p1nc
    m=p1nin*p1ncin                          
    mn+=[m]
    
plt.plot(f,mn)
plt.show()

#For p2:
def int1(t):
    return t**2
    
print integral(int1)
#n*integral of p2**2=1 so L22**2*integral(int1)*n=1
L22=math.sqrt(1/(integral(int1)))
print L22

#For p3:

#n*integral of p3**2=1 so n*integral of (L31+L33t**2)**2=1 and n*integral of p3*p1=0 so n*integral of (L31+L33t**2)*L11=0 
#this gives L31=-3/4*L33
#so L33**2*integral(int2)*n=1
def int2(t):
    return (t**2-(3.0/4.0))**2   

print integral(int2)

L33=math.sqrt(1/(integral(int2)))
print L33
L31=-(3.0/4.0)*L33
print L31

#For p4:

def int3(t):
    return t*np.sin(2*np.pi*t)

#L42=-4/9*integral(int3)*L44
def int4(t):
    return (np.sin(2*np.pi*t)-(4/9)*integral(int3)*t)**2

L44=math.sqrt(1/(integral(int4)))
L42=(-4/9)*integral(int3)*L44

#For p5:

def int5(t):
    return (t**2)*np.cos(2*np.pi*t)
#L51=(-3/4)*L53
#L53=(-20/27)*L55*integral(int5)

def int6(t):
    return (((5/9)-(20/27)*(t**2))*integral(int5)+np.cos(2*np.pi*t))**2

L55=math.sqrt(1/(integral(int6)))
L53=(-20/27)*L55*integral(int5)
L51=(-3/4)*L53


#For p8:
#n*integral of p8*p1=0 so n*integral of (L82*t+L84*sin2pi*t+L86*cos2pi*t+L88*sin4pi*t)*L11=0
def int7(t):
    return t+np.sin(2*np.pi*t)+np.cos(2*np.pi*t)+np.sin(4*np.pi*t)