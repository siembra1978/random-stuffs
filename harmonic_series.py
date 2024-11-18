import matplotlib.pyplot as plt

#nmax = int(input("n="))
#p = float(input("p="))
#t = float(input("seconds in between increments: "))

n_values = []
sum_values = []

n = 1
nmax = 10000000000
p = 2
t = .05
sum = 0

if abs(p) > 0:
    while n <= nmax:
        n_values.append(n)
        term = 1 / pow(n, p)
        sum += term
        sum_values.append(sum)

        plt.plot(n_values, sum_values, color='blue')
        plt.xlabel('n')
        plt.ylabel('Sum')
        plt.title('Sum as n increases')
        plt.grid(True)
        plt.pause(t)

        n += 1
else:
    print("absolute value of p must be greater than 0")

plt.show()
