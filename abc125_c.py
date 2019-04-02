
N = int(input())
A = [int(n) for n in input().split()]
 
from fractions import gcd
L = [0]*(N+1)
R = [0]*(N+1)
ans = 0
for i in range(N):
    L[i] = gcd(L[i-1],A[i])
for i in reversed(range(N)):
    R[i] = gcd(R[i+1],A[i])
for i in range(N):
    if gcd(L[i-1],R[i+1]) > ans:
        ans = gcd(L[i-1],R[i+1])
print(ans)
