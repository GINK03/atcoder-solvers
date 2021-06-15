

N,M,K=map(int,input().split())


dp=[[0,0] for _ in range(N+M)]
dp[0] = [1, 1]

for j in range(len(dp)-1):
    dp[j+1] = dp[j].copy()
    if K > dp[j][0] - dp[j][1]:
        dp[j+1][0] += 1
    
    if dp[j][0] < N:
        dp[j+1][0] += 1
    if dp[j][1] < M:
        dp[j+1][1] += 1

print(dp)
