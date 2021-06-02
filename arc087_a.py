import collections
N=int(input())
A=list(map(int,input().split()))
A=collections.Counter(A)

ops = 0
for k,v in A.items():
    if k > v:
        ops += v
    elif k == v:
        continue
    elif k < v:
        ops += v - k
print(ops)
