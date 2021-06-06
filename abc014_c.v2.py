import itertools
N=int(input())

L=[0]*(10**6+2)
for _ in range(N):
    a, b=map(int,input().split())
    # a=1;
    L[a] += 1
    L[b+1] -= 1

*imos,=itertools.accumulate(L)
print(max(imos))
