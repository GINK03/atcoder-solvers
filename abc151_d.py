import collections
H, W = map(int,input().split())
S = [list(input()) for h in range(H)]
G = collections.defaultdict(set)
for h in range(H):
    for w in range(W):
        ss = S[h][w]
        if ss == "#":
            continue
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh, nw = h+dh, w+dw
            if not(0 <= nh < H and 0<= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            G[(h,w)].add( (nh, nw) ) 
            G[(nh,nw)].add( (h, w) ) 
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            start = (h, w) 
            break

que = collections.deque([(start, 0)])
max_pos = (0, (-1, -1))
vis = set()
while que:
    i, cnt = que.popleft()
    if i in vis:
        continue
    max_pos = max(max_pos, (cnt, i))
    vis.add(i)
    for j in G[i]:
        if j in vis:
            continue
        que.append((j, cnt+1))
_, start = max_pos

que = collections.deque([(start, 0)])
max_pos = (0, (-1, -1))
vis = set()
while que:
    i, cnt = que.popleft()
    if i in vis:
        continue
    max_pos = max(max_pos, (cnt, i))
    vis.add(i)
    for j in G[i]:
        if j in vis:
            continue
        que.append((j, cnt+1))
ans, _ = max_pos
print(ans)
