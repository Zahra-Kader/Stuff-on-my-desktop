#Binary pulsar J0437−4715
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 1826, 1)

P0=5.757451831072007*(1.0e-3)		#Pulse Period
P1=5.72906*(1.0e-20)				#Pulse period first derivative 
ts=86400.0*t						#time in seconds
v=173.6879489990983					#rotational freq
v1=-(1/(P0**2))*P1					#rotational freq first deriv
c=3.0e8

#Keplerian parameters
Pb=5.741046*86400.0 #Pb=0.322997448930*86400.0 (Hulse)	#Orbital Period
J=Pb/2*(np.pi)											#orbital period over 2pi
e=0.000019186											#eccentricity
w=1.2													#Longitude of periastron
T0=51194.6239	#T0=52144.90097844 (Hulse)				#Epoch of periastron(MJD)
x=3.36669157											#projected semimajor axis

#Post-Keplerian parameters
wd=0.016											#Longitude of periastron derivative
Pbd=-3.64*(1.0e-12) #Pbd=-2.4184*(1.0e-12)(Hulse)	#orbital period derivative
Ts=4.925490947*(1.0e-6)								#mass of sun in time units
mp=1.76*1.989*1.0e30								#mass of pulsar
mc=0.236*1.989*1.0e30								#mass of pulsar binary companion
M=mc+mp												#combined mass
i=42.75												#orbital inclination

a1=x*c/np.sin(i)
a=x*np.sin(w)
g=e*J*(mc**2)*(mp+2*mc)/(a1*(M**2))					#gravitational redshift
B=((1-e**2)**0.5)*x*np.cos(w)
#E=np.arange(51196.69148,52927.15368,0.9476791895)

def f(E,ts,P0):
	f=E-np.sin(E)-(2*np.pi*ts)/P0
	return f
	
def bisection( eq, segment, app = 0.0000003 ):
	a, b = segment['a'], segment['b']
	Fa, Fb = eq(a,ts,P0), eq(b,ts,P0)
	if Fa * Fb > 0:
		raise Exception('No change of sign - bisection not possible')   
	while( b - a > app ): 
		E = ( a + b ) / 2.0
		f = eq(E,ts,P0)
		if f * Fa > 0: a = E
		else: b = E  
	return E

#Equation of no.of turns, N, as a function of time,t.
def N(v,ts,a,E,e,B,g,v1,J):
	N=v*(ts)-v*a*(np.cos(E)-e)-v*(B+g)*np.sin(E)-(v*((a*np.sin(E)-B*np.cos(E))*(a*(np.cos(E)-e)+B*np.sin(E)))/(J*(1-e*np.cos(E))))+(v1*(ts**2)/2)-v1*(ts)*(a*(np.cos(E)-e)+B*np.sin(E))
	return N
	
#M=arrival of next beam, i.e. completion of current turn
def R(v,ts,a,E,e,B,g,v1,J): 
	R= N(v,ts,a,E,e,B,g,v1,J).astype(int) + 1 	#current turn rounded up
	return R	

def P(ts,P0,P1):					#rotational period eqn
	P=P0+ts*P1
	return P

#L=R*P gives TOA
def L(ts,v,a,E,e,B,g,J,v1,P0,P1):
	L=R(v,ts,a,E,e,B,g,v1,J)*P(ts,P0,P1)
	return L	

plt.xlabel('Time(days)')
plt.ylabel('TOA(seconds)')
plt.plot(t,-L(ts,v,a,E,e,B,g,J,v1,P0,P1))
#plt.plot(t,N(ts,v,a,E,e,B,g,J,v1))
#plt.plot(t,E(ts,T0,J,e))
plt.show()