#for x in range (10):
	#print x**2

import numpy as np
dx=0.01
x=np.arange(0,np.pi,dx)
y=np.pi
np.sin(y)*dx
y=np.arange(0,1,dx)
import matplotlib.pyplot as plt
plt.plot(x)
plt.clf()
plt.plot(x,y)

x=np.complex(0.5,1.5)

x=np.arange (0,10,0.01)
y=np.exp(-0.5*x**2)
plt.clf()
plt.plot(x,y)