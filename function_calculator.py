import matplotlib.pyplot as plt
import numpy as np
from frange import frangef

xsolu = []
ysolu = []

xmin = -10
xmax = 10
ymin = -10
ymax = 10

amax = xmax + 1

def solve(funcs, x):
    a = funcs.replace("x", str(x))
    b = eval(a)
    #print(b)
    return b

def enter(func):

    for x in frangef(xmin, amax,.01):
        ysol = solve(func, x)
        xsolu.append(x)
        ysolu.append(ysol)

enter("2**x")

x = np.linspace(0.2,10,100)
fig, ax = plt.subplots()
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.plot(xsolu,ysolu)
plt.axis([xmin,xmax,ymin,ymax])
plt.grid(b=True)
plt.show()



