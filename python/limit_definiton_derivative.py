import math

error = .00001
min_h = 1e-10

def f(x):
    return x**3

h = .25

x = 5

while h > min_h:
    approximation = (f(x + h) - f(x))/h
    print(approximation)
    h -= error

marker_index, marker = None, None
digits = 0

for i, char in enumerate(str(approximation)):
    if char == '.':
        marker_index = i
        marker = char

    if marker_index:
        if char == '0' and i > marker_index:
            digits += 1
        elif char != '0' and i > marker_index:
            digits += 1
            break

print(round(approximation, digits))