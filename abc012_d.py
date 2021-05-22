N,M=map(int,input().split())
# import numpy as np
# G=np.zeros((N,N)) + np.inf
# G=G.tolist()
G = [[float('inf')]*N for _ in range(N)]

for i in range(0, N):
    G[i][i] = 0
for _ in range(M):
    a,b,t=map(int,input().split())
    a-=1; b-=1
    G[a][b]=t
    G[b][a]=t
# ワーシャルフロイド法
for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            G[x][y] = min(G[x][y], G[x][k] + G[k][y])
# print(np.array(G).max(axis=1).min())
print(min([max(g) for g in G]))

