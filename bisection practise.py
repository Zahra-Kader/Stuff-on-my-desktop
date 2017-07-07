import matplotlib.pyplot as plt
import numpy as np

#def a(ts):
	#a=(2*pi*ts/P0)-1
	#return a

#def b(ts):
	#b=(2*pi*ts/P0)+1
	#return b

P0=	5.757451831072007*(1.0e-3)
	
def f(E,t,P0):
	f=E-np.sin(E)-(2*np.pi*86400.0*t)/P0
	return f
	
def bisection( eq, segment, app = 0.0000003 ):
	a, b = segment['a'], segment['b']
	Fa, Fb = eq(a,t,P0), eq(b,t,P0)
	if Fa * Fb > 0:
		raise Exception('No change of sign - bisection not possible')   
	while( b - a > app ): 
		E = ( a + b ) / 2.0
		f = eq(E,t,P0)
		if f * Fa > 0: a = E
		else: b = E  
	return E
for t in range (0,1826):
	print (bisection(f,{'a':-1,'b':((2*np.pi*86400.0*1826/(5.757451831072007*1.0e-3))+1)}, 0.0000003)) #0.00003 gives the accuracy, the decimal points
#plt.plot (t,(bisection(f,{'a':-1,'b':((2*np.pi*86400.0*1826/(5.757451831072007*1.0e-3))+1)}, 0.00003)))
#plt.show()
