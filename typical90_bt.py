
H,W=map(int,input().split())

G = [list(input()) for _ in range(H)]


used = [[False] * W for _ in range(H)]
def dfs(sh, sw, ph, pw):
    if sh == ph and sw == pw and used[ph][pw] == True:
        return 0
    used[ph][pw] = True

    ret = -float("inf")
    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nh, nw = dh + ph, dw + pw
        if not (0 <= nh < H and 0<= nw < W and G[nh][nw] == "."):
            continue
        if (not(sh == nh and sw == nw)) and used[nh][nw] == True:
            continue
        v = dfs(sh, sw, nh, nw)
        ret = max(ret, v+1)
    
    used[ph][pw] = False
    return ret


ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, dfs(h, w, h, w))

if ans <= 2:
    print(-1)
else:
    print(ans)
