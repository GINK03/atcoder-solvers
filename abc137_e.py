
N,M,P=map(int,input().split())

    


G = []
for _ in range(M):
    x, y, c = map(int,input().split())
    G.append( (x-1, y-1, P-c) )


"""bellman fordで最小コスト計算"""
def bellman_ford(s: "start", N: "edge_num") -> "Optinal[List[int]]":
    d = [float("inf")]*N # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    for cnt in range(2*N):
        for fr, to, c in G:
            if d[to] > d[fr] + c:
                d[to] = d[fr] + c
                # 負閉路が存在
                if cnt == N - 1:
                    d[to] = -float("inf")
    return d

ret = bellman_ford(0, N=N)
# print(ret)

if ret[-1] != -float('inf'):
    print(max(0, -ret[-1]))
else:
    print(-1)
