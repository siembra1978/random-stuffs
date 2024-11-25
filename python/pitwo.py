import math
from siembramath import sine

nT = 10*10**309
n = 0
f = 0
ntest = 1
running = True

while running:
    try:
        f = ntest * 1.0
        ntest = (2)**(n)
        print("n = " + str(n) + "| v = " + str(ntest))
        n+=1
    except:
        running = False
        print("max n:" + str(n-1))

#f = n * sine(math.radians(180/n))

print(f)
