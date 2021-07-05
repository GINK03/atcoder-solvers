

import math

N, M = map(int, input().split())

G = [[float("inf")] * N for _ in range(N)]
for _ in range(0, M):
    u, v, c = map(int, input().split())
    u-=1; v-=1
    G[u][v] = c

# 同じノード上の距離は0とする
for i in range(0, N):
    G[i][i] = 0


log = {}
acc = 0
# ワーシャルフロイド法
for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            G[x][y] = min(G[x][y], G[x][k] + G[k][y])
            acc += G[x][y] if G[x][y] != float("inf") else 0
            
# すべての頂点の組について最短距離を計算する
#ans = 0
#for i in range(0, N):
#    for j in range(0, N):
#        ans += G[i][j]
#print(ans)
#import numpy as np 
#print(np.array(G))


print(acc)
