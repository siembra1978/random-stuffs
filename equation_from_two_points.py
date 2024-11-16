#Created By siembra (3/11/2019)

def figureitout(p1,p2,m):
    print("")
    print("y=mx+b")
    b1=p1[0]*m
    print(b1)
    b=p1[1]-b1
    print(b)
    m=str(m)
    b=str(b)
    print("Final Equation: y="+m+"x"+"+"+b)
    input("Press Enter To End The Program")

print("Created By siembra (3/11/2019)")
print("")
print("=======================================================================")
print("To Use, Enter The X and Y Values Of The First Point,")
print("Then Repeat With Point 2. Press 'Enter' Everytime you input a value.")
print("If you get a repeating decimal, don't panic. Just type the decimal")
print("into your calculator and type the repeating number until no more digits")
print("can fit into the calculator. Press 'Enter' then switch to a fraction.")
print("Open the program each time you need to compute a problem")
print("=======================================================================")
print("")
print("Point 1")
p1=(float(input("Enter X1:")),float(input("Enter Y1:")))
print(p1)

print("Point 2")
p2=(float(input("Enter X2:")),float(input("Enter Y2:")))
print(p2)

top=p2[1]-p1[1]
print(top)
bottom=p2[0]-p1[0]
print(bottom)
if bottom == 0:
    print("Undefined")
    print("ERR: Division by Zero")
    input("Press Enter To End The Program")
else:
    m=float(top/bottom)
    print(m)
    figureitout(p1,p2,m)
