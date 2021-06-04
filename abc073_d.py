
N,M,R=map(int,input().split())
*R,=map(int,input().split())
R=[r-1 for r in R]

G = [[float('inf')]*N for _ in range(N)]

for _ in range(M):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    G[a][b] = min(G[a][b], c)
    G[b][a] = min(G[b][a], c)

# ワーシャルフロイド法
for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            G[x][y] = min(G[x][y], G[x][k] + G[k][y])

import itertools

ans = float('inf')
for pt in itertools.permutations(R):
    pt =list(pt)
    cum = 0
    for i in range(len(pt)-1):
        cum += G[pt[i]][pt[i+1]]
    ans = min(cum, ans)
print(ans)
