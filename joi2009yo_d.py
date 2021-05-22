import collections
import sys
import numpy as np
sys.setrecursionlimit(2*10**6)

W=int(input())
H=int(input())

G = []
for h in range(H):
    wl = list(map(int, input().split()))
    G.append(wl)
diff = np.zeros((H,W)) + 1# [[True for _ in range(W)] for _ in range(H)]

def dfs(hw, diff, cnt):
    h,w = hw
    res = cnt
    for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nh, nw = dh+h, dw+w
        if not(0 <= nh < H and 0 <= nw < W):
            continue
        if diff[nh][nw] == 1 and G[nh][nw] == 1:
            diff[nh][nw] = 0 
            # diffは参照渡しで再帰後、リセットが必要
            # diffが必要なためqueでの管理が難しい(queではリセットができない)
            res = max(res, dfs([nh, nw], diff, cnt+1))
            diff[nh][nw] = 1
    return res

# すべての点から全探索
res = 0
for h in range(H):
    for w in range(W):
        res = max(res, dfs((h,w), diff, 0))
print(res)
