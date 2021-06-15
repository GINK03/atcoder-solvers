
import collections


N,W=map(int,input().split())
XYC = []
for _ in range(W):
    x, y, c = [int(x) for x in input().split()] # 始点,終点,コスト
    x-=1; y-=1
    XYC.append( (x,y,c) )

def dfs():
    revg = [[] for _ in range(N)]
    for x, y, c in XYC:
        revg[y].append(x)

    # dfsで到達可能判定
    q = collections.deque([N-1])
    reach = [False] * N
    while q:
        i = q.pop()
        reach[i] = True
        for j in revg[i]:
            if not reach[j]:
                q.append(j)
    return reach
reach = dfs()

"""bellman fordで最小コスト計算"""
def bellman_ford(s: "start", N: "edge_num"):
    d = [float("inf")]*N # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    for cnt  in range(N):
        update = False # 更新が行われたか
        for i, j, c in G:
            if d[j] > d[i] + c:
                d[j] = d[i] + c
                update = True
        if not update:
            break
        # 負閉路が存在
        if cnt == N - 1:
            return None
    return d

G = []
for x, y, c in XYC:
    if reach[x] and reach[y]:
        G.append( [x, y, -c] )
ret = bellman_ford(0, N)

if ret is None:
    print("inf")
else:
    print(-ret[-1])
