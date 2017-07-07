#exercise:plotting 3 gaussians with different central points(means)
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-3, 3, 500)#*
sig=1.0e-1

def gaussian(x, t, sig):
    return np.exp(-np.power(x - t, 2.) / (2 * np.power(sig, 2.)))
    #return 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - t)/sig, 2.)/2)

for t in np.arange(0,3,1):	#Do this instead of saying t=np.arange(0,3,1), latter doesnt work. reason is unclear
	plt.plot(x,gaussian(x, t, sig))#**

#For * and ** note that this plots the gaussian on the x axis from x=-3 to x=3. Omitting #* and rewriting #** to plt.plot(gaussian(np.linspace(-3, 3, 500),t,sig)) results in a gaussian plot on a random axis with a random scale (scale is not from -3 to 3)

plt.show()