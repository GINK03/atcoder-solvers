
import heapq

V, E = map(int, input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))

marked = [False] * V
marked[0] = True
count = 1
sum = 0

Q = []
for j, c in G[0]:
    heapq.heappush(Q, (c, j))

while count < V:
    c, i = heapq.heappop(Q)
    if marked[i]:
        continue
    marked[i] = True
    count += 1
    sum += c
    for (j, c) in G[i]:
        if marked[j]:
            continue
        heapq.heappush(Q, (c, j))

print(sum)
