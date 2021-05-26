import sys

N=int(input())
A=[int(input()) for _ in range(N)]

dp0 = [0] + [A[0]]
for i in range(1,N):
    dp0.append(max(dp0[-1], A[i]))

dp1 = [A[-1]]
for i in range(N-2,-1,-1):
    dp1.append(max(dp1[-1], A[i]))
dp1=list(reversed(dp1)) + [0]
#print(dp0)
#print(dp1)

for i in range(N):
    print(max(dp0[i], dp1[i+1]))
