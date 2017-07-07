
import matplotlib.pyplot as plt
from uncertainties import ufloat
import numpy as np

t = np.arange(0, 1826, 1)

v=2*(np.pi)*0.84181003670065		#angular frequency
v1=-2*(np.pi)*2.645070*(10**(-15))	#derivative 
v2=2*(np.pi)*1.2*(10**(-15))		#second derivative
ts=86400*t							#time in seconds

#Equation of pulse phase,z, as a function of time,t.
def z(ts,v,v1,v2):
	z=(ts)*v+0.5*((ts)**2)*v1+(1/6.0)*((ts)**3)*v2
	return z

#Period=1/f where f=dz/dt 
def P(ts,v,v1,v2):
	P=1/(v+ts*v1+(1/3.0)*(ts**2)*v2)
	return P

#For barycentric correction
i=4.15*(10**(-3))*(4.86/(610*10**6))#dispersion in ISM
c=3*10**8	
d=1.101587*(10**19)					#distance to pulsar
r=ufloat(0,0.01)					#position of observatory wrt barycentre

print (r)

def T(ts,r,c,d):
	T=ts+(r/c)+(r/(2*c*d))
	return T
	
#plotting a function of Period against time

plt.xlabel('Time(days)')
plt.ylabel('TOA(seconds)')
plt.plot(ts,T(ts,r,c,d))
plt.show() 