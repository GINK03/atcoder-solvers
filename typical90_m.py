
N,M=map(int,input().split())

import heapq
import collections
 
Entity = collections.namedtuple("Entity", ["node", "w"])
Entity.__lt__ = lambda self, other: self.w <= other.w

G = [[] for _ in range(N)]
for _ in range(M):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    G[a].append(Entity(b,c))
    G[b].append(Entity(a,c))


def dijkstra(start) -> "List":
    dist = [-1 for _ in range(N)]
    dist[start] = 0
    que = []
    heapq.heappush(que, Entity(start, 0))
    done = [False for _ in range(N)]
    while que:
        i, w = heapq.heappop(que)
        # すでに訪れたところは処理しない
        if done[i]:
            continue
        done[i] = True
        for j, c in G[i]:
            # 評価が未知のエッジ or より安くなる可能性がある場合は探索し、結果をヒープに入れる
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(que, Entity(j, dist[j]))
    return dist
    

A0 = dijkstra(0)
A1 = dijkstra(N-1)

for a0, a1 in zip(A0,A1):
    print(a0+a1)


