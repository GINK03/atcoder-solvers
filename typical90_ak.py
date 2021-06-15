

W, N = map(int, input().split())

LRV = []
for n in range(N):
    l, r, v = map(int, input().split())
    LRV.append((l, r, v))

dp = [[0]*(W+10) for _ in range(N+1)]
for i, (li, ri, vi) in enumerate(LRV):
    for j in range(0, W+10):
        # 検索する範囲
        cl = max(0, j - ri)
        cr = max(0, j - li + 1)
        if (cl == cr):
            continue
        val = Z[i].query(cl, cr)
        dp[i][j] = max(dp[i][j], val + V[i])
        if j >= w:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w] + v)
        else:
            dp[i+1][j] = dp[i][j]
print(dp[-1][W])
