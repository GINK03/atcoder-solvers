
N, M =map(int,input().split())


# 連立方程式
dp = [[0]*M for _ in range(N)]
for i in range(N):
    T = int(input())
    *X,=map(int,input().split())
    for x in X:
        x -= 1;
        dp[i][x] = 1

*S,=map(int,input().split())

pos = 0
for i in range(M):
    found = False
    for j in range(pos, N):
        if dp[j][i] == 1:
            if j != pos:
                dp[j], dp[pos] = dp[pos], dp[j]
            found = True
            break
    if found:
        for j in range(N):
            if j != pos and dp[j][i] == 1:
                for k in range(i, M):
                    dp[j][k] ^= dp[pos][k] # xorを取って消していく
        # このコード特有の実装
        if S[i] == 1:
            for j in range(i, M):
                S[j] ^= dp[pos][j]
        pos += 1

if S == [0]*M:
    ans = 1
    for i in range(pos, N):
        ans *= 2
        ans %= 998244353
    print(ans)
else:
    print(0)

import numpy as np
print(np.array(dp))
