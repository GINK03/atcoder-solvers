


N, M = map(int,input().split())

import heapq
import collections
 
Entity = collections.namedtuple("Entity", ["node", "w"])
Entity.__lt__ = lambda self, other: self.w <= other.w
 
G = [[] for _ in range(N)]
csum = 0
for m in range(M):
    a,b,c = map(int,input().split())
    a-=1; b-=1
    G[a].append(Entity(b,c))
    csum += c
 
def dijkstra(start, th) -> "List":
    dist = [-1 for _ in range(N)]

    done = [False for _ in range(N)]
    
    ret = 0
    for start in range(N):
        if dist[start] != -1:
            continue
        dist[start] = 0
        que = []
        heapq.heappush(que, Entity(start, 0))
        while que:
            i, w = heapq.heappop(que)
            if i > th:
                continue
                
            # すでに訪れたところは処理しない
            if done[i]:
                continue
            done[i] = True
            for j, c in G[i]:
                    # 評価が未知のエッジ or より安くなる可能性がある場合は探索し、結果をヒープに入れる
                    if dist[j] == -1 or dist[j] > dist[i] + c:
                        dist[j] = dist[i] + c
                        heapq.heappush(que, Entity(j, dist[j]))
        a = dist[-1]
        print(dist)
        ret += a
    return ret
 
cnt = collections.defaultdict(int)
for n in range(N):
    ret = dijkstra(n, n)
    if ret == -1:
        ret = 0
    print(n, csum+ret)
