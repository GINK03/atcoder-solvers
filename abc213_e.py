import collections

H, W = map(int, input().split())
G = [list(input()) for h in range(H)]

dl0 = []
for dh in [-1, 0, 1]:
    for dw in [-1, 0, 1]:
        if abs(dh) + abs(dw) >= 2 or (dh == dw == 0):
            continue
        dl0.append( (dh, dw) )
dl1 = []
for dh in [-2, -1, 0, 1, 2]:
    for dw in [-2, -1, 0, 1, 2]:
        if abs(dh) + abs(dw) >= 4 or (dh == dw == 0):
            continue
        dl1.append( (dh, dw) )


que = collections.deque([(0, 0)])
dist = [[-1] * W for _ in range(H)]
dist[0][0] = 0
while que:
    h, w = que.popleft()
    for dh, dw in dl0: 
        nh = dh + h
        nw = dw + w
        if not (0 <= nh < H and 0 <= nw < W) or dist[nh][nw] != -1:
            continue
        if G[nh][nw] == ".":
            dist[nh][nw] = dist[h][w]
            que.appendleft((nh, nw))
    for dh, dw in dl1: 
        nh = dh + h
        nw = dw + w
        if not (0 <= nh < H and 0 <= nw < W) or dist[nh][nw] != -1:
            continue
        if G[nh][nw] == "#":
            dist[nh][nw] = dist[h][w] + 1
            que.append((nh, nw))
print(dist[-1][-1])
