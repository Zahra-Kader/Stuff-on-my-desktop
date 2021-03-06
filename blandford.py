# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 22:45:48 2017

@author: Zahra
"""
from __future__ import division
from scipy.integrate import quad
import numpy as np
from sympy import solve, linsolve,symbols


from sympy import *

N=3.0                   #Number of years measurements are taken
t0=-N/2                 #lower integral limit
t1=N/2                  #upper integral limit
n=1/N                #number of measurements taken each year
J=np.complex(0,1)

def int(x):       
    ans,err=quad(x,t0,t1)
    return ans
 
#For p1:
   
def i_t0(t):            
    return t**0
def i_t2(t):
    return t**2
def i_t4(t):
    return (t**4) 
def i_tsin(t):
    return t*np.sin(2*np.pi*t)
def i_tqcos(t):
    return (t**2)*np.cos(2*np.pi*t)
def i_sinq(t):
    return (np.sin(2*np.pi*t))**2
def i_tsincos(t):
    return t*np.sin(2*np.pi*t)*np.cos(2*np.pi*t)
def i_tqcosq(t):
    return (t**2)*(np.cos(2*np.pi*t))**2
def i_cos(t):
    return np.cos(2*np.pi*t)        
def i_tcsin(t):
    return (t**3)*np.sin(2*np.pi*t)
def i_cosq(t):
    return np.cos(2*np.pi*t)**2
def i_tqsinq(t):
    return (t**2)*(np.sin(2*np.pi*t)**2)
def i_tcos(t):
    return (t)*(np.cos(2*np.pi*t))
def i_tsinf(t):
    return (t)*(np.sin(4*np.pi*t))
def i_sinfsin(t):
    return (np.sin(4*np.pi*t))*(np.sin(2*np.pi*t))
def i_tcosq(t):
    return (t)*(np.cos(2*np.pi*t))**2
def i_tsinfcos(t):
    return (t)*(np.sin(4*np.pi*t))*np.cos(2*np.pi*t)  
def i_sinfq(t):
    return (np.sin(4*np.pi*t))**2
def i_sinfcos(t):
    return (np.sin(4*np.pi*t))*np.cos(2*np.pi*t)
def i_sincos(t):
    return np.sin(2*np.pi*t)*np.cos(2*np.pi*t)
def i_tsinfsin(t):
    return (t)*(np.sin(4*np.pi*t))*np.sin(2*np.pi*t) 
L11=1.0

L22=np.sqrt(1/(n*int(i_t2)))
print L22,'22'

def third(l,m):
    return L31*l+L33*m
def fourth(q,r):
    return L42*q+L44*r
def fifth(n,o,p):
    return L51*n+L53*o+L55*p
def sixth(s,t,u):
    return L62*s+L64*t+L66*u
    
def odd_first(a,b,c,d):
    odd_first=a*int(i_t0)+b*int(i_t2)+c*int(i_cos)+d*int(i_tsin)
    return odd_first
def odd_second(a,b,c,d):
    odd_second=a*third(int(i_t0),int(i_t2))+b*third(int(i_t2),int(i_t4))+c*third(int(i_cos),int(i_tqcos))+d*third(int(i_tsin),int(i_tcsin))
    return odd_second
def odd_third(a,b,c,d):
    odd_third=a*fifth(int(i_t0),int(i_t2),int(i_cos))+b*fifth(int(i_t2),int(i_t4),int(i_tqcos))+c*fifth(int(i_cos),int(i_tqcos),int(i_cosq))+d*fifth(int(i_tsin),int(i_tcsin),int(i_tsincos))
    return odd_third
def odd_fourth(a,b,c,d):
    odd_fourth=a**2*int(i_t0)+b**2*int(i_t4)+c**2*int(i_cosq)+d**2*int(i_tqsinq)+2*a*b*int(i_t2)+2*a*c*int(i_cos)+2*a*d*int(i_tsin)+2*b*c*int(i_tqcos)+2*b*d*int(i_tcsin)+2*c*d*int(i_tsincos)-(1/n)
    return odd_fourth

def even_first(a,b,c,d):
    even_first=a*int(i_t2)+b*int(i_tsin)+c*int(i_tcos)+d*int(i_tsinf)
    return even_first
def even_second(a,b,c,d):
    even_second=a*fourth(int(i_t2),int(i_tsin))+b*fourth(int(i_tsin),int(i_sinq))+c*fourth(int(i_tcos),int(i_sincos))+d*fourth(int(i_tsinf),int(i_sinfsin))
    return even_second
def even_third(a,b,c,d):
    even_third=a*sixth(int(i_t2),int(i_tsin),int(i_tqcos))+b*sixth(int(i_tsin),int(i_sinq),int(i_tsincos))+c*sixth(int(i_tcos),int(i_sincos),int(i_tcosq))+d*sixth(int(i_tsinf),int(i_sinfsin),int(i_tsinfsin))
    return even_third
def even_fourth(a,b,c,d):
    even_fourth=a**2*int(i_t2)+b**2*int(i_sinq)+c**2*int(i_cosq)+d**2*int(i_sinfq)+2*a*b*int(i_tsin)+2*a*c*int(i_tcos)+2*a*d*int(i_tsinf)+2*b*c*int(i_sincos)+2*b*d*int(i_sinfsin)+2*c*d*int(i_sinfcos)-(1/n)
    return even_fourth
    
def psi6_first(a,b,c,d):
    psi6_first=a*int(i_t2)+b*int(i_tsin)+c*int(i_tqcos)+d*int(i_tsinf)
    return psi6_first
def psi6_second(a,b,c,d):
    psi6_second=a*fourth(int(i_t2),int(i_tsin))+b*fourth(int(i_tsin),int(i_sinq))+c*fourth(int(i_tqcos),int(i_tsincos))+d*fourth(int(i_tsinf),int(i_sinfsin))
    return psi6_second
def psi6_third(a,b,c,d):
    psi6_third=a*sixth(int(i_t2),int(i_tsin),int(i_tqcos))+b*sixth(int(i_tsin),int(i_sinq),int(i_tsincos))+c*sixth(int(i_tcos),int(i_sincos),int(i_tcosq))+d*sixth(int(i_tsinf),int(i_sinfsin),int(i_tsinfsin))
    return psi6_third
def psi6_fourth(a,b,c,d):
    psi6_fourth=a**2*int(i_t2)+b**2*int(i_sinq)+c**2*int(i_tqcosq)+d**2*int(i_sinfq)+2*a*b*int(i_tsin)+2*a*c*int(i_tqcos)+2*a*d*int(i_tsinf)+2*b*c*int(i_tsincos)+2*b*d*int(i_sinfsin)+2*c*d*int(i_sinfcos)-(1/n)
    return psi6_fourth

def const(f,var1,var2):
    var1,var2=symbols('var1 var2')
    const=solve([f],(var1,var2))
    u=const[0]
    var1=float(u[0])
    var2=float(u[1])
    #var3=float(u[2])
    return var1,var2
#print const(f=odd_first(L31,L33,0,0),odd_fourth(L31,L33,0,0),var1=L31,var2=L33)

L31,L33=symbols('L31 L33')
const_3=solve([odd_first(L31,L33,0,0),odd_fourth(L31,L33,0,0)],(L31,L33))
u3=const_3[0]
L31=float(u3[0])
L33=float(u3[1])
print const_3
print L33

L42,L44=symbols('L42 L44')
const_4=solve([even_first(L42,L44,0,0),even_fourth(L42,L44,0,0)],(L42,L44))
u4=const_4[0]
L42=float(u4[0])
L44=float(u4[1])


#L42=-0.310785320218 
#L44=1.46454131826 
#L62=-0.0885912262039 
#L64=-0.101559488534 
#L66=-1.63059907714 
#L51=-0.120095065498 
#L53=0.160126753998 
#L55=1.42234894439 
L51,L53,L55=symbols('L51 L53 L55')
const_5=solve([odd_first(L51,L53,L55,0),odd_second(L51,L53,L55,0),odd_fourth(L51,L53,L55,0)],(L51,L53,L55))
u5=const_5[0]
L51=float(u5[0])
L53=float(u5[1])
L55=float(u5[2])
print L51,'51'
print L53,'53'
print L55,'55'

L62,L64,L66=symbols('L62 L64 L66')
const_6=solve([psi6_first(L62,L64,L66,0),psi6_second(L62,L64,L66,0),psi6_fourth(L62,L64,L66,0)],(L62,L64,L66))
u6=const_6[0]
L62=float(u6[0])
L64=float(u6[1])
L66=float(u6[2])
print L62,'62'
print L64,'64'
print L66,'66'



L82,L84,L88=symbols('L82 L84 L88')
const_8=linsolve([even_first(L82,L84,0,L88),even_second(L82,L84,0,L88)],(L82,L84,L88))
print const_8,'8'
#print type(const_8)
#L82=float(const_8.pop()) #removes and returns the first element of the set
#L84=float(const_8.pop())
L88=symbols('L88')
#print solve([even_fourth(L82,L84,0, L88)],(L88)),'8'
L88=1.42719598251935
L82=0.11378948564214*L88
L84=-0.0362203182236615*L88

L71,L73,L75,L77=symbols('L71 L73 L75 L77')
const_7=linsolve([odd_first(L71,L73,L75,L77),odd_second(L71,L73,L75,L77),odd_third(L71,L73,L75,L77)],(L71,L73,L75,L77))
print const_7,'7'
L77=symbols('L77')
print solve([odd_fourth(0.195747170028813*L77, -0.473202817494278*L77, 0.0316320019745384*L77, L77)],L77),'7'
L77=2.03888188067173
L71=0.195747170028813*L77
L73=-0.473202817494278*L77
L75=0.0316320019745384*L77