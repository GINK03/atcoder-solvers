
import heapq
import collections

MOD = 10**9 + 7
N,M  =map(int,input().split())
 
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

dp = [0 for n in range(N)]
dp[0] = 1
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
                dp[j] = dp[i] # 値の初期化
                heapq.heappush(que, Entity(j, dist[j]))
            elif dist[j] == dist[i] + c:
                dp[j] += dp[i] # 前のnodeを次のnodeに加える
                dp[j] %= MOD
    return dist
dist = dijkstra2(0)
print(dp[N-1])
