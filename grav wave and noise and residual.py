# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 16:46:49 2017

@author: Zahra
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:16:42 2017

@author: Zahra
"""

from scipy.interpolate import UnivariateSpline
from scipy.signal import savgol_filter
import numpy as np
from matplotlib import pyplot as plt
from blandford import L31,L42,L44,L22,L33,L62,L64,L66,L51,L53,L55,L71,L73,L75,L77,L82,L84,L88

siy=3.1536e7
N=3.0
m=1024
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
nu=nu/siy
L11=1.0
L86=0.4

#Radio Telescope Effelsberg 
Trec_sky=22+3 #Trec_sky=33 meerkat
G=2.2 #meerkat
bandwidth=1100.0 #850MHz bandwidth for meerkat
S=0.73
t_int=120.0*60.0
W=31.7*1e-3
P=1.187913
sig=Trec_sky*W**(1.5)/(S*G*np.sqrt(t_int)*np.sqrt(bandwidth)*np.sqrt(P))
print sig

def fitfunc(f):
    f[0:fz]=0
    f[sz:m]=0
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

fitfunc_sum=y1(L11)+y2(L22)+y3(L31,L33)+y4(L42,L44)+y5(L51,L53,L55)+y6(L62,L64,L66)+y7(L71,L73,L75,L77)+y8(L82,L84,L86,L88)
T=1.0-(fitfunc_sum)

spl = UnivariateSpline(nu, T)
sp1=spl.set_smoothing_factor(4)
sav=savgol_filter(T,35,2)
b_gauss=N/2
a_gauss=-N/2
spacing=(b_gauss-a_gauss)/m
t_gauss=np.arange(a_gauss,b_gauss,spacing) #np.arange works better than np.linspace for large number of points?

def powerspec(f):
    f=(np.fft.fft(f))/m   #Divide by the number of non zero terms
    f=np.fft.fftshift(f)    # Shift zero freq to center
    f_sq=np.absolute(f)**2 
    return f_sq

sig=1e-15/siy
y_gauss=np.exp(-0.5*(t_gauss-0)**2/(sig)**2) #white noise in time domain

omega_gw=1e-15
H0=1e-10/siy #Hubbles constant in hertz 
P0=omega_gw*(H0**2)/(8*np.pi**4)
P=P0*nu**(-5) #grav wave spectrum in frequency domain
Pbh=(nu*siy)**(-13.0/3.0)*1e-30/(12*np.pi**2)*siy**3 #Eqn (1) from THE NANOGRAV NINE-YEAR DATA SET: LIMITS ON THE ISOTROPIC STOCHASTIC GRAVITATIONAL WAVE BACKGROUND
#notice that in this part of the eqn (f/yr^-1)^(-13/3), the f/yr^-1 is dimensionless

hb=np.sqrt(12.0)*np.pi*((nu)**(3.0/2.0))*np.sqrt(Pbh)
#hb_epta=3e-15*(nu*siy)**(-2.0/3.0) ...this is the characteristic strain for smbh from epta, Gravitational waves: Classification, Methods of detection, Sensitivities, and Sources
#hb_alt=1e-15*(nu*siy)**(-2.0/3.0)
hn=np.sqrt(12.0)*np.pi*((nu)**(3.0/2.0))*np.sqrt(powerspec(y_gauss))/T
hn_smt=np.sqrt(12.0)*np.pi*((nu)**(3.0/2.0))*np.sqrt(powerspec(y_gauss))/spl(nu)
hn_sav=np.sqrt(12.0)*np.pi*((nu)**(3.0/2.0))*np.sqrt(powerspec(y_gauss))/sav

hc=np.sqrt(12.0)*np.pi*((nu)**(3.0/2.0))*np.sqrt(P)

plt.loglog(nu,hc,'r')
plt.loglog(nu,hn_smt,'g')
plt.loglog(nu,hn,'c')
plt.loglog(nu,hb,'b')
#plt.loglog(nu,hb_alt,'r')
plt.loglog(nu,hn_sav,'m')
#plt.loglog(nu,spl(nu),'r')
#plt.loglog(nu,T,'m')
#plt.loglog(nu,P)
#plt.plot(t_gauss,y_gauss) 
#plt.plot(nu,powerspec(y_gauss)) #the sigma is in units of time and then take the fft and square it to get units of freq squared. Dont input gaussian of variance and then take fft
#plt.loglog(nu,P*T)
#plt.plot(nu,2.0/T)
#plt.xlim(0,10e-7)
#plt.ylim(0,1e-12)
plt.show()

