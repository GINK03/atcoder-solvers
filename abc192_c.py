import math

N, K = map(int, input().split())


def cal(x):
    tmp = [int(a) for a in str(x)]

    right = 0
    for idx, a in enumerate(sorted(tmp)):
        size = len(tmp)
        right += a * 10 ** (size - idx -1)

    left = 0
    for idx, a in enumerate(sorted(tmp, key=lambda x:-x)):
        size = len(tmp)
        left += a * 10 ** (size - idx - 1)

    return left - right

cyc = {}
x = N
for k in range(10**5+1):
    if cyc.get(k-1) == x:
        cyc[k] = x
        continue
    cyc[k] = x
    #print(x)
    x = cal(x)
#print(cyc)
print(cyc[K])
