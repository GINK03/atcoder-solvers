import collections
import numpy as np
W,H=map(int,input().split())

G = np.zeros((H+2, W+2)).astype(int).tolist()
for h in range(1,H+1):
    for w, s in enumerate(map(int,input().split()), 1):
        G[h][w] = s
Vis = np.zeros((H+2, W+2)).astype(int).tolist()

def bfs(que):
    walls = 0
    while que:
        h, w, cnt = que.popleft()
        if Vis[h][w]:
            continue
        Vis[h][w] = 1
        if h % 2 == 0:
            action = ((-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1))
        else:
            action = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1))
        for dh, dw in action:
            nh,nw=dh+h,dw+w
            if 0 <= nh < H+2 and 0 <= nw < W+2:
                # 0 -> 1
                if G[nh][nw] == 1:
                    walls += 1
                else:
                    que.append( (nh, nw, cnt) )
            else:
                continue
    return walls 

que = collections.deque([(0,0,0)])
walls = bfs(que)
print(walls)
