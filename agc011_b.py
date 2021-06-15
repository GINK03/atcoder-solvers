import itertools
N=int(input())
*A,=map(int,input().split())
A.sort()

*C,=itertools.accumulate(A)

tmp = 0
for i in range(N-1):
    if C[i]*2 < A[i+1]:
        tmp = i+1
print(N-tmp)

