import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3, 3, 500)

def gaussian(x):
	return np.exp(-np.power(x,2.0))
	
plt.plot(x,gaussian(x))
plt.show()