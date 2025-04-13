n = 10
known = [1,2]

result = 0

for i in range(1,n-1):
    next = 2*known[i] + 3*known[i-1]
    known.append(next)

print(known)