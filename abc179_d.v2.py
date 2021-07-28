N,K = map(int,input().split())

MOD = 998244353
LR = []
for k in range(K):
    L,R = map(int,input().split())
    LR.append((L,R+1))

dp = [0]*(N+1)
dp[0] = 1
dp[1] = -1
for i in range(N):
    if i > 0:
        dp[i] += dp[i-1]
    for l, r in LR:
        if i + l < N:
            dp[i+l] += dp[i] 
            dp[i+l] %= MOD
        if i + r < N:
            dp[i+r] -= dp[i]

print(dp[N-1] % MOD)
