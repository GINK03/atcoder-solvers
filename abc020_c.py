
import heapq
import collections

H, W, T = map(int,input().split())
G = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if G[h][w] == "S":
            s = (h, w)
        if G[h][w] == "G":
            t = (h, w)

def dijkstra(s: "Tuple", G, CMax):
    dist = collections.defaultdict(lambda :float("INF"))
    dist[s] = 0
    done = collections.defaultdict(lambda :False)

    que = []
    heapq.heapify(que)
    heapq.heappush(que, (0,s)) # 距離d, 頂点iの順
    while que:
        d, i = heapq.heappop(que)
        if done[i]:
            continue
        done[i] = True
        for dh,dw in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            jh, jw = i[0] + dh, i[1] + dw
            if not (0 <= jh < H and 0 <= jw < W):
                continue
            if G[jh][jw] == "#":
                c = CMax
            elif G[jh][jw] == "G":
                c = 1
            else:
                c = 1
            j = (jh,jw)
            if dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(que, (dist[j], j))
    return dist 


def is_ok(n):
    dist = dijkstra(s, G, CMax=n)
    if dist[t] <= T:
        return True
    else:
        return False

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(10**20, 0))

