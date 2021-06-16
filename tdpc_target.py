

import bisect
N = int(input())

XR = []
for _ in range(N):
    x, r = map(int,input().split())
    XR.append( (x-r, x+r) )
XR.sort(reverse=True)
R = [r for l,r in XR]

dp = [float("inf")]*(N)
for a in R:
    # 単調減少数列
    # 以下の処理は単調減少の数を求める
    idx = bisect.bisect_left(dp, a)
    dp[idx] = a
print(sum(1 for x in dp if x < float("inf")))

