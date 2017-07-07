import matplotlib.pyplot as plt
import numpy as np

sig=1.0e-1

def gaussian(x,t,sig):
	return np.exp(-np.power(x-t,2.0)/(2*np.power(sig,2.0)))
	
for t in np.arange(0,3,1):
	plt.plot(t,gaussian(np.linspace(-3, 3, 500),t,sig))

plt.show()