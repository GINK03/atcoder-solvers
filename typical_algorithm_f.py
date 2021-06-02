
import heapq
import collections
N, M = map(int, input().split())
G=collections.defaultdict(list)
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))

# 初期化
que, visited = [], set([0])
[heapq.heappush(que, (c, j)) for j, c in G[0]]

ans = 0
while que:
    c, i = heapq.heappop(que)
    if visited.__contains__(i):
        continue
    visited.add(i) 
    ans += c
    for (j, nc) in G[i]:
        if visited.__contains__(j):
            continue
        heapq.heappush(que, (nc, j))
print(ans)
