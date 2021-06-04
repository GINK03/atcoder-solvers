

N,X,Y=map(int,input().split())
X-=1; Y-=1
import heapq
import collections


Entity = collections.namedtuple("Entity", ["node", "w"])
Entity.__lt__ = lambda self, other: self.w <= other.w

G = [[] for _ in range(N)]
for n in range(N-1):
    G[n].append(Entity(n+1,1))
    G[n+1].append(Entity(n,1))
G[X].append(Entity(Y, 1))
G[Y].append(Entity(X, 1))

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

cnt = collections.defaultdict(int)
for n in range(N):
    dist = dijkstra(n)
    # print(dist)
    for i in range(n+1, N):
        cnt[dist[i]] += 1 

for k in range(1, N):
    print(cnt[k])

