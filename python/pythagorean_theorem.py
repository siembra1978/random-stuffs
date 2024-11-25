#Created by siembra (3/18/2019)
import math

def findmissingleg(a,c):
    asquared=a*a
    csquared=c*c
    bsquared=csquared-asquared
    b=math.sqrt(bsquared)
    bsquared=str(bsquared)
    b=str(b)
    print("Before Square: "+bsquared)
    print("Original: "+b)
    input("Press Any Key To Continue...")

a=input("Enter Leg A: ")
c=input("Enter Hypotenuse: ")
a=float(a)
c=float(c)
findmissingleg(a,c)
