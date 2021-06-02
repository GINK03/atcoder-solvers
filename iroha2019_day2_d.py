
import heapq
import collections
N, M = map(int, input().split())

G = collections.defaultdict(list)
for node_num in range(M):
    u, v, c = map(int, input().split())
    u-=1; v-=1
    G[u].append((v, -c, node_num))
    G[v].append((u, -c, node_num))


que = []
# 初期化
[heapq.heappush(que, (c, j, node_num)) for j, c, node_num in G[0]]
visited = set([0])

traces = []
while que:
    c, i, node_num = heapq.heappop(que)
    if i in visited:
        continue
    visited.add(i)
    traces.append(node_num+1)
    for (j, nc, nnode_num) in G[i]:
        if j in visited:
            continue
        heapq.heappush(que, (nc, j, nnode_num))

traces.sort()
print(*traces, sep="\n")
