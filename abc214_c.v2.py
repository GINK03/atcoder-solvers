import collections
import heapq
 
Entity = collections.namedtuple("Entity", ["node", "w"])
Entity.__lt__ = lambda self, other: self.w <= other.w

N = int(input())
*S, = map(int, input().split())
*T, = map(int, input().split())

G = collections.defaultdict(list)
for i in range(N):
    G[-1].append( (i, T[i]) )

for i in range(N):
    G[i].append( ((i+1)%N, S[i]) )

def dijkstra(start) -> "List":
    # dist = [-1 for _ in range(N)]
    dist = collections.defaultdict(lambda :-1)
    done = collections.defaultdict(lambda :False)
    dist[start] = 0
    que = []
    heapq.heappush(que, Entity(start, 0))
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

# print(G)
dist = dijkstra(-1)
for i in range(N):
    print(dist[i])
