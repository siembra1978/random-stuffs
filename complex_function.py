# Created in Desmos by max
# Rewritten in Python by siembra

import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import hsv_to_rgb

def f(x,y):
    #return ((((1+(5**.5))/2)**complex(x,y)) - ((1-(5**.5))/2)**complex(x,y))/(5**.5)
    #return (complex(x,y)**2)
    return ((x/y)*complex(x,y))
    #return cmath.sqrt(-1)**x

R = 10
D = 6
s = 11
C = np.arange(-R,R + 1/D,1/D)

bound = 25

a_values = np.arange(-R, R + 1/D, 1/D)
b_values = np.arange(-R, R + 1/D, 1/D)

points = []

i = 0

total = len(C)**2

for a in a_values:
    for b in b_values:
        hue = ((s*np.imag(f(a,b)))%360)/360
        sat = 1
        value = 1

        hsv = (hue,sat,value)

        color = hsv_to_rgb(hsv)

        i+=1
        #point = (float(a),float(b), np.real(f(a,b)), color)
        point = (float(a),float(b), np.real(f(a,b)), color)
        print(f'{(i/total)*100:.2f}% | {i}/{total}')
        points.append(point)

#print("Points: ",len(points))

x,y,z,colors = zip(*points)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,c=colors,marker='o')

ax.set_xlim(left=-bound)
ax.set_xlim(right=bound)
ax.set_ylim(bottom=-bound)
ax.set_ylim(top=bound)
ax.set_zlim(bottom=-bound)
ax.set_zlim(top=bound)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('complex function')

plt.show()