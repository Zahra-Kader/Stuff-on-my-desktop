#Isolated pulsar PSR B1133+16
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 1826, 1)

v=0.84181003670065					#rotational frequency(non angular)
v1=-2.645070*(1.0e-15)				#freq first derivative 
v2=1.2*(1.0e-15)					#freq second derivative 
ts=86400.0*t						#time in seconds
P0=1.1879164614374982				#Period
P1=-(P0**2)*v1						#period first derivative 
P2=2*(P0**3)*(v1**2)-(P0**2)*v2		#period second derivative 
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

#Period	
def P(ts,P0,P1,P2):
	P=P0+ts*P1+0.5*((ts)**2)*P2
	return P

#L=M*P gives TOA
def L(ts,v,v1,v2,P0,P1,P2):
	L=M(ts,v,v1,v2)*P(ts,P0,P1,P2)+np.random.normal(0,1.378326292e-4,1826)
	return L
	
#To get timing residual, omit v&v2 from model, get TOA(new) and subtract from TOA(old)	

vn=0.84181003670065					#rotational frequency(non angular)
v1n=-2.645070*(1.0e-16)				#freq first derivative 
v2n=1.2*(1.0e-15)					#freq second derivative 
P0n=1.1879164614374982				#Period
P1n=-0*(P0n**2)*v1n						#period first derivative
P2n=2*(P0n**3)*(v1n**2)-(P0n**2)*v2n		#period second derivative 
#alternative P2: P2=(2/P0)*(P1**2)-(P0**2)*v2

def Nn(ts,vn,v1n,v2n):
	Nn=(ts)*vn+0.5*((ts)**2)*v1n+(1/6.0)*((ts)**3)*v2n
	return Nn

#M=arrival of next beam, i.e. completion of current turn
def Mn(ts,vn,v1n,v2n): 
	#M=np.ceil((ts)*v+0.5*((ts)**2)*v1+(1/6.0)*((ts)**3)*v2)
	Mn= Nn(ts,vn,v1,v2n).astype(int) + 1 	#current turn rounded up
	return Mn	
	
def Pn(ts,P0n,P1n,P2n):
	Pn=P0n+ts*P1n+0.5*((ts)**2)*P2n
	return Pn
	
def Ln(ts,vn,v1n,v2n,P0n,P1n,P2n):
	Ln=Mn(ts,vn,v1n,v2n)*Pn(ts,P0n,P1n,P2n)
	return Ln	

def K(ts,v,v1,v2,P0,P1,P2,vn,v1n,v2n,P0n,P1n,P2n):
	K=L(ts,v,v1,v2,P0,P1,P2)-Ln(ts,vn,v1n,v2n,P0n,P1n,P2n)
	return K
	
#plotting a function of TOA against time

plt.xlabel('Time(days)')
plt.ylabel('Timing residual(seconds)')
#plt.plot(t,Ln(ts,vn,v1,v2n,P0,P1,P2n))
plt.plot(t,K(ts,v,v1,v2,P0,P1,P2,vn,v1n,v2n,P0n,P1n,P2n))
#plt.plot(t,-L(ts,v,v1,v2,P0,P1,P2))
#plt.plot(t,M(ts,v,v1,v2))
plt.show()