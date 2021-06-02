H,W=map(int,input().split())

G = [list(input()) for _ in range(H)]

# イラストを描いて理解しないと難しい
res = []
for h in range(H-1):
    for w in range(W-1):
        r = 0
        for dh, dw in [(0,0), (1, 0), (0, 1), (1,1)]:
            nh = h + dh
            nw = w + dw
            r += 1 if G[nh][nw] == '#' else 0
        if r == 3 or r == 1:
            res.append((h,w))

print(len(res))
