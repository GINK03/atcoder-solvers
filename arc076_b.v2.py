
import heapq
import collections
N = int(input())
G = collections.defaultdict(list)

XY = []
for _ in range(N):
    x,y = map(int, input().split())
    XY.append( (x,y) )


XY.sort()
for i in range(N-1):
    x, y = XY[i]
    nx, ny = XY[i+1]
    cost = min(abs(x-nx), abs(y-ny))
    G[(x,y)].append( ((nx,ny), cost) )
    G[(nx,ny)].append( ((x,y), cost) )
XY.sort(key=lambda x:x[1])
for i in range(N-1):
    x, y = XY[i]
    nx, ny = XY[i+1]
    cost = min(abs(x-nx), abs(y-ny))
    G[(x,y)].append( ((nx,ny), cost) )
    G[(nx,ny)].append( ((x,y), cost) )

que = []
start = XY[0]
# 初期化(prim法的には任意のどこからでも初めて良い)
[heapq.heappush(que, (c, xy)) for xy, c in G[start]]
visited = set([start])

acc = 0
while que:
    c, i = heapq.heappop(que)
    if i in visited:
        continue
    visited.add(i)
    acc += c
    for (j, nc) in G[i]:
        if j in visited:
            continue
        heapq.heappush(que, (nc, j))
print(acc)
