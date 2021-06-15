
H,W=map(int,input().split())

G=[]
for h in range(H):
    G.append(list(input()))

import collections
import heapq

if G[0][0] == "#":
    cnt = 1
else:
    cnt = 0
que = [(0, 0, 0, cnt)]


vis = set()
while que:
    _, h,w,cnt = heapq.heappop(que)
    if (h,w) == (H-1,W-1):
        print((cnt + 1)//2)
        break
    if (h,w) in vis:
        continue
    vis.add((h,w))

    for dh, dw in [(1,0), (0, 1)]:
        nh, nw = h+dh, w+dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue    
        if (nh,nw) in vis:
            continue
        if G[h][w] != G[nh][nw]:
            heapq.heappush(que, (cnt+1, nh, nw, cnt+1) )
        else:
            heapq.heappush(que, (cnt, nh, nw, cnt) )

