from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np 

#initialize a normal distribution with frozen in mean=-1, std. dev.= 1
rv = norm(loc = -1., scale = 1.0)
rv1 = norm(loc = 0., scale = 2.0)
rv2 = norm(loc = 2., scale = 3.0)

x = np.arange(-10, 10, .1)

#plot the pdfs of these normal distributions 
plt.plot(x, rv.pdf(x), x, rv1.pdf(x), x, rv2.pdf(x))