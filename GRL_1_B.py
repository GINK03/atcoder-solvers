
V,E,R=map(int,input().split())

G = []
for _ in range(E):
    x, y, c = map(int,input().split())
    G.append( (x, y, c) )

    
"""bellman fordで最小コスト計算"""
def bellman_ford(s: "start", N: "edge_num") -> "Optinal[List[int]]":
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

ret = bellman_ford(R, N=V)
if ret is None:
    print("NEGATIVE CYCLE")
else:
    ret = ["INF" if r == float("inf") else r for r in ret]
    print(*ret, sep="\n")
