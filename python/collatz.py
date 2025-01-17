import random

r = 10000000000000000000000000000000000000000000000000000000000000
#r = 100

while True:
    n = r
    i = r
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        steps += 1

    print(f"Started with: {i}, Ended with {n}, Took {steps} steps")
    r += 1