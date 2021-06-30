

MOD = 10**9 + 7
N,L=map(int,input().split())

dp = [0]*(N+1)
dp[0] = 1

for i in range(len(dp)):
    for j in [1, L]:
        if i+j < len(dp):
            dp[i+j] += dp[i]
            dp[i+j] %= MOD

print(dp[N])
