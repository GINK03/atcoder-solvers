B=10**9+7
s=int(input())

x = [0, 0, 1, 1, 1, 2, 3]

for i in range(2000):
    n = (x[-1] + x[-3])%B
    x.append(n)

print(x[s-1])
