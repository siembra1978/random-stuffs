import math
import time
import matplotlib.pyplot as plt

xmax = float(eval(input("max x: ")))
# xmax = 25
xstep = float(eval(input("x step: ")))
# xstep = 1
funcU = str(input("enter function: "))
t = float(input("time spacing: "))

x_values = []
output_values = []

x = 1

while x <= xmax:
    output = eval(funcU)
    x_values.append(x)
    output_values.append(output)

    print("x=" + str(x) + ", ans=" + str(output))
    plt.plot(x_values, output_values, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('graph')
    plt.grid(True)
    plt.pause(t)

    x += xstep

plt.show()
