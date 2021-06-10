
from typing import List, Any
import sys; sys.setrecursionlimit(10**9)

def dfs1(N: int) -> List[int]:
    """深さを記録する"""
    I = []
    used = [False]*N
    def _dfs(pos):
        used[pos] = True
        for i in G[pos]:
            if used[i] == False:
                _dfs(i)
        I.append(pos)
    for i in range(N):
        if used[i] == False:
            _dfs(i)
    return I

def dfs2(RI: List[int]) -> Any:
    """逆順に遅い値から見ていく
    遅い値から見るとdfs1でスキップされた経路を探索でき、
    その経路は巡回になっていれば閉じて終わる"""
    def _dfs(pos, grp):
        used[pos] = True
        grp.append(pos)
        for i in H[pos]:
            if used[i] == False:
                _dfs(i, grp)
    used = [False]*N

    igrp = []
    for i in RI:
        grp = []
        if used[i]:
            continue
        _dfs(i, grp)
        igrp.append(grp)
    return igrp

N,M=map(int,input().split())
G=[[] for _ in range(N)]
H=[[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    # a-=1; b-=1
    G[a].append(b)
    H[b].append(a)

I=dfs1(N)
igrp = dfs2(I[::-1]) ; """逆にしてインプットする"""
*igrp, = filter(lambda x:x, igrp)
l = len(igrp)
print(l)
for grp in igrp:
    print(len(grp), *grp[::-1])


