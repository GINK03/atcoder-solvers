import numpy as np
import collections
H, W = map(int,input().split())
sx,sy=map(int,input().split())
que = collections.deque([(sx-1,sy-1, 0)])

gx,gy=map(int,input().split())
gx-=1
gy-=1

G=[]
for _ in range(H):
    G.append(list(input()))
#G = np.array(G)
while que:
    h,w,cnt = que.popleft()
    if G[h][w] == '.':
        G[h][w] = cnt
    else:
        continue
    for dh,dw in ((1,0), (0,1), (-1, 0), (0, -1)):
        nh, nw = h+dh, w+dw
        if not(0 <= nh < H and 0<= nw < W):
            continue
        if G[nh][nw] == '.':
            que.append( (nh, nw, cnt+1) )
#print(*G, sep='\n')
print(G[gx][gy])
