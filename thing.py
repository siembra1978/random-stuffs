import time
from sympy import *

a = symbols('x')

factorial_as_gamma = gamma(a+1)
gamma_derivative = diff(factorial_as_gamma, a)

def harmonic_sum(x):
    sum = 0
    n=1
    while n <= x:
        sum += 1/(2*n)
        n+=1
    return sum

def line(x):
    return (((gamma_derivative.subs(a,x).evalf()) / factorial(x)) + (1 - (gamma_derivative.subs(a,1).evalf())))/2

x = 0
sig_figs = 10

while True:
    g = round(harmonic_sum(x),sig_figs)
    h = round(line(x),sig_figs)

    if str(g) == str(h):
        print(x, g, h)
    else:
        print("awkward")

    x += 1
    #time.sleep(.25)