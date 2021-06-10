import itertools
N=int(input())
*A,=map(int,input().split())

T=sum(A)
*C,=itertools.accumulate(A)

ans = float("inf")
for i in range(N-1):
    right = T-C[i]
    left = C[i] 
    ans = min(ans, abs(right-left))
print(ans)

