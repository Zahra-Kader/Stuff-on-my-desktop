#Isolated pulsar PSR B1133+16
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 1826, 1)

v=0.84181003670065					#rotational frequency(non angular)
v1=-2.645070*(1.0e-15)				#freq first derivative 
v2=1.2*(1.0e-15)					#freq second derivative 
ts=86400.0*t						#time in seconds
P0=1/v								#Period
P1=-0*(P0**2)*v1						#period first derivative 
P2=(2/(v**3))*(v1**2)-(P0**2)*v2	#period second derivative 
#alternative P2: P2=(2/P0)*(P1**2)-(P0**2)*v2

#Equation of no. of turns,N, as a function of time,t.
def N(ts,v,v1,v2):
	N=(ts)*v+0.5*((ts)**2)*v1+(1/6.0)*((ts)**3)*v2
	return N

#M=arrival of next beam, i.e. completion of current turn
def M(ts,v,v1,v2): 
	#M=np.ceil((ts)*v+0.5*((ts)**2)*v1+(1/6.0)*((ts)**3)*v2)
	M= N(ts,v,v1,v2).astype(int) + 1 	#current turn rounded up
	return M

#frequency 
def f(ts,v,v1,v2):
	f=v+ts*v1+0.5*((ts)**2)*v2
	return f

#Period	
def P(ts,P0,P1,P2):
	P=P0+ts*P1+0.5*((ts)**2)*P2
	return P

#L=M*P gives TOA
def L(ts,v,v1,v2,P0,P1,P2):
	L=M(ts,v,v1,v2)*P(ts,P0,P1,P2)
	return L
	
#plotting a function of TOA against time

plt.xlabel('Time(days)')
plt.ylabel('TOA(seconds)')
plt.plot(t,L(ts,v,v1,v2,P0,P1,P2))
#plt.plot(t,M(ts,v,v1,v2))
plt.show()