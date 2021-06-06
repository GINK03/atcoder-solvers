import itertools
N,M=map(int,input().split())

A = [0]*M

s_sum = 0
for _ in range(N):
    l,r,s = map(int, input().split())
    A[l-1] += s
    if r < M:
        A[r] -= s
    s_sum += s
*imos,=itertools.accumulate(A)
print(s_sum - min(imos))




