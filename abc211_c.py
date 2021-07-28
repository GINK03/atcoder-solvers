
import collections
S= input()
MOD = 1000000007

def mimi_dp(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0]*(n2+1) for _ in range(n1+1)]
    dp[0][0] = 1
    for i in range(n1):
        for j in range(n2+1):
            dp[i+1][j] += dp[i][j] # 下に流す
        for j in range(n2):
            if s1[i] == s2[j]: # 同じならば
                dp[i+1][j+1] += dp[i][j] # 加えていく
        for j in range(n2+1): # 横をMOD
            dp[i+1][j] %= MOD
    print(dp[n1][n2])

mimi_dp(s1=S, s2="chokudai")

