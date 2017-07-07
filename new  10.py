from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-3, 2000, 5000)
sig=1.0e-4

def gaussian(x, mu, sig):
    #return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    #return 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)
	return np.exp(-np.power((x - mu)/sig, 2.)/2.)
for mu in np.arange(0,1826,1):
    plt.plot(x,gaussian(x, mu, sig))

plt.show()