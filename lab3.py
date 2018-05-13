from pylab import *
from scipy.integrate import odeint
t = arange(0, 100.0, 0.001)
y0 = [1.0, 1.0]
om=1
mu=1
k=1
lamb=1
eps = 0.0
def vanDerPole(y, t):
    return [y[1],-om*om*y[0]+mu*(1-y[0]*y[0])*y[1]+k*y[0]*cos(lamb*t)]

def Plot(func,title_):
    y = odeint(func, y0, t)
    subplot(2, 1, 1)
    plot(t, y, linewidth=0.7)
    xlabel('Time')
    ylabel('Placement & velocity')
    title('Placement & velocity for '+title_+' oscillator')
    grid(True)
    subplot(2, 1, 2)
    plot(y[:,0], y[:,1], linewidth=0.6)
    xlabel('')
    ylabel('')
    title('Phase portrait for '+title_+' equation')
    grid(True)

Plot(vanDerPole, "VanDerPole")
show()
