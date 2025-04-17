import random
import time

#r = 10000000000000000000000000000000000000000000000000000000000000
r = 1

while True:
    n = r
    steps = 0
    highest = r
    streak = 0

    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1
        
        if n > highest:
            highest = n

        steps += 1
        time.sleep(.5)

    time.sleep(.125)
    print(f"Started with: {r}, Took {steps} steps, Highest was {highest}")
    r += 1