#Created By siembra (3/18/2019)
import math

print("Created By siembra (3/18/2019)")
print("")
print("Point 1")
p1=(float(input("Enter X1:")),float(input("Enter Y1:")))
print(p1)

print("Point 2")
p2=(float(input("Enter X2:")),float(input("Enter Y2:")))
print(p2)

top=p1[0]-p2[0]
print(top)
bottom=p1[1]-p2[1]
print(bottom)
tops=top*top
bottoms=bottom*bottom
d1=tops+bottoms
d=math.sqrt(d1)
print(d1)
print(d)
input("Press Any Key To Continue")
