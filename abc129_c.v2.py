
N, M = map(int,input().split())
MOD = 10**9 + 7
A = [int(input()) for _ in range(M)]
A = set(A)

dp = [0]*(N+2)
dp[0] = 1

for i in range(len(dp)):
    if i+2 not in A:
        if i+2 <= N:
            dp[i+2] += dp[i]
            dp[i+2] %= MOD
            
    if i+1 not in A:
        if i+1 <= N:
            dp[i+1] += dp[i]
            dp[i+1] %= MOD

print(dp[N]%MOD)
    



