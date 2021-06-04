
SA,SB,X,Y=map(int,input().split())
SA-=1;
SB-=1;
N=202
G = [[]*N for _ in range(N)]

A = [a for a in range(100)]
B = [b+100 for b in range(100)]

for i in range(len(A)-1):
    G[A[i]].append( (A[i+1], Y) )
    G[A[i+1]].append( (A[i], Y) )

for i in range(len(B)-1):
    G[B[i]].append( (B[i+1], Y) )
    G[B[i+1]].append( (B[i], Y) )

for i in range(0, len(A)):
    G[B[i]].append( (A[i], X) )
    G[A[i]].append( (B[i], X) )

for i in range(1, len(A)):
    G[B[i-1]].append( (A[i], X) )
    G[A[i]].append( (B[i-1], X) )

import collections
import heapq
Entity = collections.namedtuple("Entity", ["node", "w"])
Entity.__lt__ = lambda self, other: self.w <= other.w

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

dist = dijkstra(SA)
#print(dist)
print(dist[SB+100])
