import collections

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

P = [[-1] * W for _ in range(H)]
P[sh][sw] = 0

que = collections.deque([(sh, sw)])

while que:
    h, w = que.popleft()
    for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nh = dh + h
        nw = dw + w
        if not (0 <= nh < H and 0 <= nw < W and P[nh][nw] == -1):
            continue
        if G[nh][nw] == '#':
            P[nh][nw] = P[h][w] + 1
            que.append((nh, nw))
        elif G[nh][nw] in {".", "g"}:
            P[nh][nw] = P[h][w]
            que.appendleft((nh, nw))

print("YES" if P[gh][gw] <= 2 else "NO")
