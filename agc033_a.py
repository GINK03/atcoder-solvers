import collections

H, W = map(int, input().split())

G = []
for h in range(H):
    arr = list(input())
    G.append(arr)

que = collections.deque([])
param = [[-1] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if G[h][w] == '#':
            que.append((h, w))
            param[h][w] = 0
        else:
            param[h][w] = -1

d=0
while que:
    h, w = que.popleft()
    d = param[h][w]
    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nh = a + h
        nw = b + w
        
        if nh > H - 1 or nh < 0 or nw < 0 or nw > W - 1:
            continue
        if param[nh][nw] == -1:
            que.append((nh, nw))
            param[nh][nw] = param[h][w]+1
print(d)

