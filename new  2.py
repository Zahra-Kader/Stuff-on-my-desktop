#Binary pulsar J0437−4715
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 1826, 1)

P0=5.757451831072007*(1.0e-3)		#Pulse Period
P1=5.72906*(1.0e-20)				#Pulse period first derivative 
ts=86400.0*t						#time in seconds
v=1/P0								#rotational freq
v1=-(1/(P0**2))*P1					#rotational freq first deriv

#print (v)
#print (v1)

#Equation of no.of turns, N, as a function of time,t.
def N(ts,v,v1):
	N=(ts)*v+0.5*((ts)**2)*v1
	return N

#M=arrival of next beam, i.e. completion of current turn
def M(ts,v,v1): 
	M=np.ceil((ts)*v+0.5*((ts)**2)*v1)
	#M= N(ts,v,v1).astype(int) + 1 	#current turn rounded up
	return M
	
def P(ts,P0,P1):
	P=P0+ts*P1
	return P

def Q(ts,P0,P1):
	Q=2*(np.pi)/P(ts,P0,P1)		#angular velocity/frequency=2(pi)f	
	return Q
	
#L=M*P gives TOA
def L(ts,v,v1,P0,P1):
	L=M(ts,v,v1)*P(ts,P0,P1)
	return L
	
#binary system
#Keplerian parameters

Pb=5.741046*86400.0			#Orbital Period
e=0.000019186				#eccentricity
w=1.2						#Longitude of periastron
T0=51194.6239				#Epoch of periastron	
x=3.36669157				#projected semimajor axis

#Post-Keplerian parameters
wd=0.016					#Longitude of periastron derivative
pbd=3.64					#orbital period derivative
Ts=4.925490947*(1.0e-6)		#mass of sun in time units
mp=1.76*1.989*1.0e30		#mass of pulsar
mc=0.236*1.989*1.0e30		#mass of pulsar binary companion
i=42.75						#orbital inclination

rd=1900.0					#radius of pulsar

def A(mp,Q,rd):					#radial acceleration for graph of rad.acc against period (lorimer)
	A=mp*((Q(ts,P0,P1))**2)*rd
	return A

def gr(Pb,Ts,mp,mc): 		#gravitational redshift
	gr=(np.e)*((Pb/2*(np.pi))**(1/3))*(Ts**(2/3))*((mp+mc)**(-4/3))*mc(mp+2*mc)
	return gr
	
def rs(Ts,mc):
	rs=Ts*mc				#shapiro delay parameter
	return rs
	
def s(i):					#shapiro delay parameter
	s=np.sin(i)
	return s

#plotting a function of TOA against time

plt.xlabel('Period(seconds)')
plt.ylabel('Acceleration')
plt.plot(t, L(ts,v,v1,P0,P1))
#plt.plot(A(mp,Q,rd),P(ts,P0,P1))
plt.show() 