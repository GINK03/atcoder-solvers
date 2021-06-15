
import heapq
import collections

Entity = collections.namedtuple("Entity", ["node", "w"])
Entity.__lt__ = lambda self, other: self.w <= other.w

H,W = map(int,input().split())
N = H*W

sh, sw = map(int,input().split())
sh-=1; sw-=1
start = sh*W + sw
eh, ew = map(int,input().split())
eh-=1; ew-=1
end = eh*W + ew

M = []
for h in range(H):
    M.append(list(input()))

"""
G = [[] for _ in range(N)]
for h in range(H):
    for w in range(W):
        frm_idx=h*W + w
        for dh,dw in [(1, 0), (-1,0), (0,1), (0,-1)]:
            nh,nw=h+dh,w+dw
            if 0 <= nh < H and 0 <= nw < W:
                to_idx=nh*W+nw
                if M[nh][nw] == ".":
                    G[frm_idx].append(to_idx)
""" 
 
def bfs(start):
    que = collections.deque([(start, 0, 0)])
    dist = [float("inf")]*N
    while que:
        i, dir, c = que.popleft()
        dist[i] = c
        for dh, dw, dd in [(1, 0, 0), (-1,0, 1), (0,1, 2), (0,-1, 3)]:
            h, w = i//W, i%W
            nh,nw=h+dh,w+dw
            if not(0 <= nh < H and 0 <= nw < W):
                continue
            if M[nh][nw] != ".":
                continue
            if i == start:
                nc = 0
            else:
                if dir != dd:
                    nc = 1
                else:
                    nc = 0
            nidx=nh*W+nw
            if dist[nidx] > c+nc:
                que.append( (nidx, dd, c+nc) )
    return dist
    
dist = bfs(start) 
# print(dist)
print(dist[end])
