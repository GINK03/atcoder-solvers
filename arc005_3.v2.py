import collections
import heapq

H, W = map(int, input().split())

G = []
for h in range(H):
    G.append(list(input()))

for h in range(H):
    for w in range(W):
        if G[h][w] == 's':
            sh, sw = h, w
        if G[h][w] == 'g':
            gh, gw = h, w

que = [(0, sh, sw)]
dist=collections.defaultdict(lambda :-1)
heapq.heapify(que)

while que:
    c, h, w = heapq.heappop(que)
    dist[(h, w)] = c
    for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nh = dh + h
        nw = dw + w
        if not (0 <= nh < H and 0 <= nw < W):
            continue
        if dist[(nh, nw)] != -1:
            continue
        if G[nh][nw] == '#':
            heapq.heappush(que, (c+1, nh, nw) )
        elif G[nh][nw] in {".", "g"}:
            heapq.heappush(que, (c, nh, nw) )

if dist[(gh, gw)] <= 2:
    print("YES")
else:
    print("NO")
