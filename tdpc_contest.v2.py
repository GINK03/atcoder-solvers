
N=int(input())
*P,=map(int,input().split())

dp = [[0]*(sum(P) + 10) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(sum(P)+10):
        dp[i+1][j] = dp[i][j]
        if j - P[i] >= 0:
            dp[i+1][j] += dp[i][j-P[i]]
print(len(list(filter(lambda x:x>0,dp[-1]))))
