
import collections
class Entry:
    def __init__(self, to, cap, backward):
        self.to = to
        self.cap = cap
        self.backward = backward

class Dinic:
    def __init__(self, N: int):
        '''
        Args:
            N (int): グラフのエッジ数(V)
        '''
        self.N = N
        self.G = [[] for i in range(N)]

    def add(self, fr, to, cap):
        forward = Entry(to=to, cap=cap, backward=None)
        forward.backward = backward = Entry(to=fr, cap=0, backward=forward)
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s: int, t: int) -> int:
        # level変数は階層の深さ
        self.level = level = [None]*self.N
        que = collections.deque([s])
        level[s] = 0
        G = self.G
        while que:
            v = que.popleft()
            lv = level[v] + 1
            for ne in G[v]:
                if ne.cap and level[ne.to] is None:
                    level[ne.to] = lv
                    que.append(ne.to)
        return level[t] is not None

    def dfs(self, s: int, t: int, f, trs: "List[int]") -> int:
        if s == t:
            trs.append(s); return f
        level = self.level
        for ne in self.it[s]:
            if ne.cap and level[s] < level[ne.to]:
                d = self.dfs(ne.to, t, min(f, ne.cap), trs)
                if d > 0:
                    ne.cap -= d
                    ne.backward.cap += d
                    trs.append(s); return d
        trs.append(s); return 0

    def flow(self, s: int, t: int) -> int:
        flow = 0
        INF = float('inf') # 10**9 + 7
        G = self.G
        gtrs = []
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                trs = []
                f = self.dfs(s, t, INF, trs)
                if f > 0:
                    gtrs.append(trs[::-1])
                flow += f
        return flow, gtrs


H, W = map(int, input().split())
B = [list(input()) for _ in range(H)]
S,T = H*W, H*W+1

dinic = Dinic(H*W+2)

for h in range(H):
    for w in range(W):
        if B[h][w] == "#":
            continue
        # スタートと偶数地点を連結
        x = h*H + w
        if (h + w) % 2 == 0:
            dinic.add(S, x,  1) 
            for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nh = dh+h
                nw = dw+w
                if 0 <= nh < H and 0 <= nw < W and B[nh][nw] == ".":
                    y = nh*W + nw
                    dinic.add(x, y, 1)
        else: # 奇数フィールドではゴールに連結
            dinic.add(x, T, 1)

flow, gtrs = dinic.flow(S,T)
print(flow)

dic = {}
for h in range(H):
    for w in range(W):
        i = h * W + w
        dic[i] = (h,w)
for trs in  gtrs:
    l,r = trs[1:3]
    x0,y0 = dic[l]
    x1,y1 = dic[r]
    if (x0+y0)%2 == 0:
        if x0 - x1 == 1:
            B[x0][y0] = "^"
            B[x1][y1] = "v"
        if x0 - x1 == -1:
            B[x0][y0] = "v"
            B[x1][y1] = "^"
        if y0 - y1 == 1:
            B[x0][y0] = "<"
            B[x1][y1] = ">"
        if y0 - y1 == -1:
            B[x0][y0] = ">"
            B[x1][y1] = "<"

for b in B:
    print(*b, sep="")
"""
        if (i + j) % 2 == 0:
            for y in flow[x]:
                di, dj = y // m - i, y % m - j
 
                if di == -1:
                    board[i][j] = "^"
                    board[i + di][j + dj] = "v"
                if di == 1:
                    board[i][j] = "v"
                    board[i + di][j + dj] = "^"
                if dj == -1:
                    board[i][j] = "<"
                    board[i + di][j + dj] = ">"
                if dj == 1:
                    board[i][j] = ">"
                    board[i + di][j + dj] = "<"
"""
