N, W = map(int, input().split())

VW = []
for n in range(N):
    v, w = map(int, input().split())
    VW.append((v, w))

dp = [[0]*(W+10) for _ in range(N+1)]

for i, (v, w) in enumerate(VW):
    for j in range(0, W+10):
        if j >= w:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w] + v)
        else:
            dp[i+1][j] = dp[i][j]

#import numpy as np
#print(np.array(dp))
#print(np.array(dp)[-1, W])
print(dp[-1][W])
