
N,M=map(int,input().split())


ABCD = []
for _ in range(M):
    *abcd, = map(int,input().split())
    ABCD.append(abcd)

import heapq
import collections
 
Entity = collections.namedtuple("Entity", ["node", "w", "w2"])
Entity.__lt__ = lambda self, other: self.w <= other.w


min_cost = float('inf')
def check(T, is_check=False):
    global min_cost
    G=[[] for _ in range(N)]
    for a,b,c,d in ABCD:
        a-=1; b-=1
        t = T
        G[a].append(Entity(b,c + d//(t+1),d))
        G[b].append(Entity(a,c + d//(t+1),d))

     
    def dijkstra(start) -> "List":
        dist = [-1 for _ in range(N)]
        dist[start] = 0
        que = []
        heapq.heappush(que, Entity(start, 0, 0))
        done = [False for _ in range(N)]
        while que:
            i, w, _ = heapq.heappop(que)
            # すでに訪れたところは処理しない
            if done[i]:
                continue
            done[i] = True
            for j, c, d in G[i]:
                # 評価が未知のエッジ or より安くなる可能性がある場合は探索し、結果をヒープに入れる
                if dist[j] == -1 or dist[j] > dist[i] + c - d//(T+1) + d//(T + dist[i] + 1):
                    dist[j] = dist[i] + c - d//(T+1) + d//(T + dist[i] + 1)
                    heapq.heappush(que, Entity(j, dist[j], d))
        return dist

    dist = dijkstra(0)
    if is_check:
        return T + dist[-1]

    if min_cost > T + dist[-1]:
        min_cost = T + dist[-1]
        return True
    else:
        return False

if check(0, is_check=True) == -1:
    print("-1")
    exit()
#print(check(1))
#print(check(2))

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok

t = meguru_bisect(ok=10**8, ng=0)
print(check(t, is_check=True))
