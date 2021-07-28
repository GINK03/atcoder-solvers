
MOD = 10**9 + 7
N,M  =map(int,input().split())
import heapq
import collections
 
Entity = collections.namedtuple("Entity", ["node", "w"])
Entity.__lt__ = lambda self, other: self.w <= other.w
 
G = [[] for _ in range(N)]
for m in range(M):
    a, b = map(int,input().split())
    a-=1; b-=1
    G[a].append(Entity(b,1))
    G[b].append(Entity(a,1))
 
def dijkstra(start) -> "List":
    dist = [-1 for _ in range(N)]
    dist[start] = 0
    que = []
    heapq.heappush(que, Entity(start, 0))
    done = [False for _ in range(N)]
    while que:
        i, w = heapq.heappop(que)
        if done[i]:
            continue
        done[i] = True
        for j, c in G[i]:
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(que, Entity(j, dist[j]))
    return dist
 
DIST = dijkstra(0)
if DIST[-1] == -1:
    print(0)
    exit()

cont = [0 for n in range(N)]
cont[0] = 1
def dijkstra2(start) -> "List":
    dist = [-1 for _ in range(N)]
    dist[start] = 0
    que = []
    heapq.heappush(que, Entity(start, 0))
    done = [False for _ in range(N)]
    while que:
        (i, w) = heapq.heappop(que)
        for (j, c) in G[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + c
                cont[j] = cont[i]
                heapq.heappush(que, Entity(j, dist[j]))
            elif dist[j] == dist[i] + c:
                cont[j] += cont[i]
                cont[j] %= MOD
    return dist
#print(DIST)
dist = dijkstra2(0)
print(cont[N-1])
