import math
P = int(input())

x = [math.factorial(i) for i in range(1, 11)]

acc = 0

for x0 in x[::-1]:
    if P//x0 > 0:
        acc +=  P//x0
        P%=x0

print(acc)
