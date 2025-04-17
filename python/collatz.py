import random
import time

#r = 10000000000000000000000000000000000000000000000000000000000000
r = 1

while True:
    n = r
    i = r
    steps = 0
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        steps += 1
        time.sleep(.5)

    print(f"Started with: {i}, Ended with {n}, Took {steps} steps")
    r += 1