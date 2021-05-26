import sys
N,K,Q=map(int,input().split())
A = [int(input()) for n in range(Q)]
dp =[K-Q]*N

for a in A:
    a-=1
    dp[a] += 1

for x in dp:
    if x > 0:
        print("Yes")
    else:
        print("No")

