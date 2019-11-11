from collections import Counter
N = int(input())
Ds = list(map(int, input().split()))

if Ds[0] != 0:
    print(0)
    exit()
Ds = sorted(Ds[1:])
c = Counter(Ds)
M = 998244353

r = p = i = 1
x = c.get(i)
while x:
    N -= x
    r = r * pow(p, x, M) % M
    i += 1; p = x; x = c.get(i)
print((r,0)[N>1])
