
import math

N, M = map(int, input().split())
mat = [[math.inf] * N for _ in range(N)]

for _ in range(0, M):
    u, v, c = map(int, input().split())
    mat[u][v] = c

# 同じノード上の距離は0とする
for i in range(0, N):
    mat[i][i] = 0

# ワーシャルフロイド法
for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            mat[x][y] = min(mat[x][y], mat[x][k] + mat[k][y])

# 負の閉路(negative cycle)を検出
flag = False
for i in range(N):
    if mat[i][i] < 0:
        flag = True

if flag:
    print("NEGATIVE CYCLE")
else:
    for elms in mat:
        print(*[elm if elm != math.inf else "INF" for elm in elms])
