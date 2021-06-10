
import collections
# from dataclasses import dataclass
# from typing import Optional
# @dataclass
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

    def dfs(self, s: int, t: int, f) -> int:
        if s == t:
            return f
        level = self.level
        for ne in self.it[s]:
            if ne.cap and level[s] < level[ne.to]:
                d = self.dfs(ne.to, t, min(f, ne.cap))
                if d > 0:
                    ne.cap -= d
                    ne.backward.cap += d
                    return d
        return 0

    def flow(self, s: int, t: int) -> int:
        flow = 0
        INF = float('inf') # 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

N = int(input())

A = [[i] + list(map(int,input().split())) for i in range(N)]
B = [[i+N] + list(map(int,input().split())) for i in range(N)]

AB = A + B
S = 2*N 
T = 2*N + 1
dinic = Dinic(2*N + 2)
for ai in range(N):
    dinic.add(S, ai, 1) # source
    for bi in range(N, 2*N):
        _, ax, ay = AB[ai] 
        _, bx, by = AB[bi]
        if ax < bx and ay < by:
            dinic.add(ai,bi, 1)
    
for bi in range(N, 2*N):
    dinic.add(bi, T, 1)

print(dinic.flow(S,T))
