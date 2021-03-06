
import collections
# from dataclasses import dataclass
# from typing import Optional
# @dataclass
class Entry:
    def __init__(self, to, cost, backward):
        self.to = to
        self.cost = cost
        self.backward = backward

class Dinic:
    def __init__(self, N: int):
        '''
        Args:
            N (int): グラフのエッジ数(V)
        '''
        self.N = N
        self.G = [[] for i in range(N)]

    def add(self, fr: int, to: int, cost: int):
        forward = Entry(to=to, cost=cost, backward=None)
        forward.backward = backward = Entry(to=fr, cost=0, backward=forward)
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi(self, v1, v2, cost1, cost2):
        edge1 = [v2, cost1, None]
        edge1[2] = edge2 = [v1, cost2, edge1]
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
                if ne.cost and level[ne.to] is None:
                    level[ne.to] = lv
                    que.append(ne.to)
        return level[t] is not None

    def dfs(self, s: int, t: int, f) -> int:
        if s == t:
            return f
        level = self.level
        for ne in self.it[s]:
            if ne.cost and level[s] < level[ne.to]:
                d = self.dfs(ne.to, t, min(f, ne.cost))
                if d > 0:
                    ne.cost -= d
                    ne.backward.cost += d
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


'''
4 5
0 1 2
0 2 1
1 2 1
1 3 1
2 3 2
'''
V,E=map(int,input().split())
dinic = Dinic(N=V)
for _ in range(E):  
    u, v, c = map(int,input().split())
    dinic.add(u, v, c)

print(dinic.flow(0,V-1))
