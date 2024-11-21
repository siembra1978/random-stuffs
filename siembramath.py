import math

pi = 3.14

def getPiArchimedes():
    n = 10*10**307
    f = n * sine(math.radians(180/n))
    return f

def factorial(input):
    if input != 0:
        i = input-1
        r = input
        while i > 0:
            r = r*i
            i-=1
        return r
    else:
        return 1

def sine(input):
    running = True
    sinn = 0
    sineSum = 0
    while running:
        try:
            if sinn <= 100:
                appendent = ((-1)**sinn)*((input**((2*sinn)+1))/(factorial((2*sinn)+1)))
                sineSum+=appendent
                sinn+=1
            else:
                return sineSum
        except:
            running = False
            return sineSum

def cosine(input):
    running = True
    cosn = 0
    cosineSum = 0
    while running:
        try:
            if cosn <= 100:
                appendent = ((-1)**cosn)*((input ** (2 * cosn)) / (factorial((2 * cosn))))
                cosineSum+=appendent
                cosn+=1
            else:
                return cosineSum
        except:
            running = False
            return cosineSum
            #print("n=" + str(n))

def tan(input):
    top = sine(input)
    bottom = cosine(input)
    return top/bottom

if __name__ == "__main__":
    pi = getPiArchimedes()

    inputv = pi/6

    print(f'pi = {pi}')
    print(f'sine = {sine(inputv)}')
    print(f'cosine = {cosine(inputv)}')
    print (f'tangent = {tan(inputv)}')