
# 問題文の意図を読み取るのがすごい大変だった
# もう一度やったほうがいい
import copy
N=int(input())
B=[list(map(int,input().split())) for _ in range(N)]

G = copy.deepcopy(B)

xys = set()
# ワーシャルフロイド法
for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            # 別の道路による最短経路の組み合わせがあるということ
            if x!=k and y != k and G[x][y] == G[x][k] + G[k][y]:
                xys.add( (x,y) )
            G[x][y] = min(G[x][y], G[x][k] + G[k][y])

if B != G:
    print(-1)
else:
    ans = 0
    for x in range(N):
        for y in range(N):
            if not (x, y) in xys:
                ans += G[x][y]
    print(ans//2)

