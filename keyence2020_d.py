
N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())

dp = [[float("inf")]*N for _ in range(1<<N)]
for i in range(N):
    dp[1<<i][i] = 0

for i in range(1<<N):
    cnt = bin(i).count('1')
    for j in range(N):
        if dp[i][j] < float('inf'):
            

