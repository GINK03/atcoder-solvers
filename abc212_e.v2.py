
MOD = 998244353
N, M, K = map(int, input().split())
G = [[] for n in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    u -=1 ; v -= 1
    G[u].append(v)
    G[v].append(u)

dp = [[0] * N for k in range(K+1)]
dp[0][0] = 1

for k in range(K):
    s = sum(dp[k])
    for n in range(N):
        dp[k+1][n] = s - dp[k][n]
        for j in G[n]:
            dp[k+1][n] -= dp[k][j]
    for n in range(N):
        dp[k+1][n] %= MOD
# print(dp)
print(dp[-1][0]%MOD)


