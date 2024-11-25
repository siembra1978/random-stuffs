#Created By siembra (3/11/2019)
x=0
y=0
m=0
b=0
z=0

def yeet(x,y,m,z):
    print("y=mx+b")
    print(y+"="+"("+m+")"+x+"+b")
    x=float(x)
    y=float(y)
    m=float(m)
    x2=m*x
    x=str(x)
    x2=str(x2)
    y=str(y)
    m=str(m)
    print(y+"="+x+"+b")
    x=float(x)
    x2=float(x2)
    y=float(y)
    m=float(m)
    b=y-x2
    x=str(x)
    x2=str(x2)
    y=str(y)
    m=str(m)
    b=str(b)
    print(y+"="+x+"+"+b)
    print("y="+m+"x"+"+"+b)
    
print("Created By siembra (3/11/2019)")
print("")
print("========================================================================")
print("To use, enter the X value, the Y value, and the 'M' value AKA the slope.")
print("Press Enter To Compute The Problem")
print("Open the program each time you need to compute a problem")
print("========================================================================")
print("")
x=input("Enter X: ")
y=input("Enter Y: ")
m=input("Enter M: ")
x=str(x)
y=str(y)
m=str(m)
yeet(x,y,m,z)
input("Press Enter To End The Program")

