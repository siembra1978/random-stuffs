from siembramath import sine
import math

def approximate_pi(n):
    f = n * sine(math.radians(180/n))
    return f

#n = 10*10**307
n=1
while True:
    print(f'pi ~= {approximate_pi(n):.75f}')
    n+=1