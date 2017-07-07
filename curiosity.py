import math
def function(x,A,B):
	return math.exp(A*x)*math.sin(B*x)

import matplotlib.plyplot as plt
points=1e4
xmin, xmax=-1,5
xlist=map(lambda x: float(xmax-xmin)*x/points,range(points+1))
ylist=map(lambda y: function(y,-1,5),xlist)
plt.plot(xlist,ylist)
plt.show