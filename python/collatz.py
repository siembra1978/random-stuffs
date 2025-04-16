import random
import time

#r = 10000000000000000000000000000000000000000000000000000000000000
r = 1

while True:
    n = r
    i = r
    steps = 0
    highest = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        
        if n > highest:
            highest = n

        steps += 1

    time.sleep(.25)
    print(f"Started with: {i}, Ended with {n}, Took {steps} steps, Highest was {highest}")
    r += 1