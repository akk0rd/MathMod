from pylab import *
from scipy.integrate import odeint
y0 = [0.0, 0.1, 0.0, 0.0]
m=1
k=1
l=10.0
g=9.8
def func(y, t):
	a=l+g/k-y[2]
	b=sqrt(y[0]*y[0]+a*a)
	v=-k*y[0]*(1-l/b)
	w=-g+k*(1-l/b)*a
	return [y[1],v,y[3],w]
t = arange(0, 1200.0, 0.001)
y = odeint(func, y0, t)
plot(y[:,0], y[:,2], linewidth=0.6)
xlabel('x position')
ylabel('y position')
title('Spring oscillations in vertical plain')
grid(True)
show()