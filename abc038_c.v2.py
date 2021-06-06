N = int(input())
*A, = map(int,input().split())

B = []
for i in range(len(A)-1):
    B.append(int(A[i] < A[i+1]))

import itertools
cum = 0
for gk,vs in itertools.groupby(B):
    if gk == 0:
        continue
    n = len(list(vs))
    cum += n * (n+1) // 2
print(cum + N)


