
N=int(input())
A=list(map(int,input().split()))
 
import math
ans = math.inf
 
patterns = 1<<N
for i in range(1, patterns):
    tmp, total = 0, 0
    for j in range(N):
        tmp |= A[j]
        if i&(1<<j) > 0:
            total ^= tmp
            tmp = 0
    total ^= tmp
    ans = min(ans, total)
print(ans)

