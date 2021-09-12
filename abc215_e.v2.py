
MOD = 998244353
N = int(input())
S = input()

P = 1 << 10 # せいぜい10種類のコンテストしかないので1024の表現で間に合う
dp = [[[0]*10 for i in range(P)] for j in range(N+1)]
for i in range(1, N+1):
    x = ord(S[i-1]) - ord("A")
    for u in range(P):
        for j in range(10):
            dp[i][u][j] = dp[i-1][u][j]
            if j == x:
                dp[i][u][j] += dp[i-1][u][j]
                dp[i][u][j] %= MOD

    for v in range(P):
        if v & (1<<x) > 0:
            continue
        for j in range(10):
            dp[i][v|(1<<x)][x] += dp[i-1][v][j]
            dp[i][v|(1<<x)][x] %= MOD

    dp[i][(1<<x)][x] += 1
    dp[i][(1<<x)][x] %= MOD


ans = 0 
for u in range(P):
    for j in range(10):
        ans += dp[N][u][j] 
        ans %= MOD
print(ans)
