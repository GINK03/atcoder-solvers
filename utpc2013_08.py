

N,M=map(int,input().split())

*P,=map(int,input().split())
*Q,=map(int,input().split())


XYAB = []
for _ in range(M):
    xyab = list(map(int,input().split()))
    XYAB.append(xyab)

G = []
for i, p in enumerate(P):
    G.append( (2*N, i, p) )
    G.append( (i, 2*N, 0) )

for i, q in enumerate(Q):
    G.append( (2*N, i+N, 0) )
    G.append( (i+N, 2*N, q) )

for x,y,a,b in XYAB:
    x -= 1;
    y += N-1
    G.append( (x, y, -a) )
    G.append( (y, x, b) )


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

        if d[-1] != 0:
            return "no"
    return "yes"

d = bellman_ford(2*N, N=2*N+1)
print(d)
