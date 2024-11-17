import random

r = 1

while True:
    n = r
    i = r
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
    print(f"Started with: {i}, Ended with {n}")
    r += 1