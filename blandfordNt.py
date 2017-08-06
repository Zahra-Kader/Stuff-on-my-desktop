# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:12:48 2017

@author: Zahra
"""

from __future__ import division
from scipy.integrate import quad
import numpy as np
from sympy import solve, linsolve,symbols

from sympy import *

N=10.0                   #Number of years measurements are taken
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
print int(i_t2),'t2'
def i_t4(t):
    return (t**4) 
def i_tsin(t):
    return t*np.sin(2*np.pi*t)
print int(i_tsin),'tsin'
def i_tqcos(t):
    return (t**2)*np.cos(2*np.pi*t)
print int(i_tqcos),'tqcos'
def i_sinq(t):
    return (np.sin(2*np.pi*t))**2
print int(i_sinq),'sinq'
def i_tsincos(t):
    return t*np.sin(2*np.pi*t)*np.cos(2*np.pi*t)
print int(i_tsincos),'tsincos'
def i_tqcosq(t):
    return (t**2)*(np.cos(2*np.pi*t))**2
print int(i_tqcosq),'tqcos'
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

L22t=np.sqrt(1/(n*int(i_t2)))

def third(l,m):
    return L31t*l+L33t*m
def fourth(q,r):
    return L42t*q+L44t*r
def fifth(n,o,p):
    return L51t*n+L53t*o+L55t*p
def sixth(s,t,u):
    return L62t*s+L64t*t+L66t*u
    
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

L311,L331=symbols('L311 L331')
const_3=solve([odd_first(L311,L331,0,0),odd_fourth(L311,L331,0,0)],(L311,L331))
u3=const_3[0]
L31t=float(u3[0])
L33t=float(u3[1])

L421,L441=symbols('L421 L441')
const_4=solve([even_first(L421,L441,0,0),even_fourth(L421,L441,0,0)],(L421,L441))
u4=const_4[0]
L42t=float(u4[0])
L44t=float(u4[1])


#L42=-0.310785320218 
#L44=1.46454131826 
#L62=-0.0885912262039 
#L64=-0.101559488534 
#L66=-1.63059907714 
#L51=-0.120095065498 
#L53=0.160126753998 
#L55=1.42234894439 
L511,L531,L551=symbols('L511 L531 L551')
const_5=solve([odd_first(L511,L531,L551,0),odd_second(L511,L531,L551,0),odd_fourth(L511,L531,L551,0)],(L511,L531,L551))
u5=const_5[0]
L51t=float(u5[0])
L53t=float(u5[1])
L55t=float(u5[2])

L62,L64,L66=symbols('L62 L64 L66')
const_6=solve([psi6_first(L62,L64,L66,0),psi6_second(L62,L64,L66,0),psi6_fourth(L62,L64,L66,0)],(L62,L64,L66))
u6=const_6[0]
L62t=float(u6[0])
L64t=float(u6[1])
L66t=float(u6[2])
print L62t,'62'
print L64t,'64'
print L66t,'66'

L821,L841,L881=symbols('L821 L841 L881')
const_81=linsolve([even_first(L821,L841,0,L881),even_second(L821,L841,0,L881)],(L821,L841,L881))
print const_81,'8'
L881=symbols('L881')
print solve([even_fourth(0.00960770442457665*L881,0.00305822730187473*L881,0, L881)],(L881)),'8'
L88t=0.140791767451380
L82t=0.00960770442457665*L88t
L84t=0.00305822730187473*L88t

L711,L731,L751,L771=symbols('L711 L731 L751 L771')
const_71=linsolve([odd_first(L711,L731,L751,L771),odd_second(L711,L731,L751,L771),odd_third(L711,L731,L751,L771)],(L711,L731,L751,L771))
print const_71,'7'

L771=symbols('L771')
print solve([odd_fourth(-0.234535775340849*L771, 0.0472428862119292*L771, 0.074790766396274*L771, L771)],L771),'7'
L77t=0.0226474862718359
L71t=-0.234535775340849*L77t
L73t=0.0472428862119292*L77t
L75t=0.074790766396274*L77t
