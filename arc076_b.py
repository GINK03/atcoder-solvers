import collections
import heapq

N = int(input())
XY = [list(map(int,input().split())) + [i] for i in range(N)]
G = collections.defaultdict(list)
XY.sort()
for i in range(N-1):
    d = 1
    sx, sy, si = XY[i]
    tx, ty, ti = XY[i+d]
    c = min(abs(tx - sx), abs(ty - sy))
    G[si].append( (ti, c) )
    G[ti].append( (si, c) )
XY.sort(key=lambda x:x[1])
for i in range(N-1):
    d = 1
    sx, sy, si = XY[i]
    tx, ty, ti = XY[i+d]
    c = min(abs(tx - sx), abs(ty - sy))
    G[si].append( (ti, c) )
    G[ti].append( (si, c) )


N = len(G)
marked = set()
count = 1
sum = 0

Q = []

# 最初は手動探査
for j, c in G[0]:
    heapq.heappush(Q, (c, j))
marked.add(0)

while Q:
    c, i = heapq.heappop(Q)
    if i in marked:
        continue
    marked.add(i)
    sum += c
    for (j, nc) in G[i]:
        if j in marked:
            continue
        heapq.heappush(Q, (nc, j))
print(sum)
    
    

