import math

error = .000001
min_h = 1e-10

def factorial(input):
    if input != 0:
        i = input-1
        r = input
        while i > 0:
            r = r*i
            i-=1
        return r
    else:
        return 1

def f(x):
    return math.gamma(x+1)

h = 1

x = 1

print('h')

while h > min_h:
    print((f(x + h) - f(x))/h)
    h -= error