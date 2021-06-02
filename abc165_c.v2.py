import itertools
import sys; sys.setrecursionlimit(10**9)
N,M,Q=map(int,input().split())

D = []
for _ in range(Q):
    *x,=map(int,input().split())
    D.append(x)

"""
ans = 0
for pt in itertools.combinations_with_replacement(list(range(1,M+1)), N):
    cum = 0
    for a,b,c,d in D:
        if pt[b-1] - pt[a-1] == c:
            cum += d
    ans = max(ans, cum)
print(ans)
"""

ans = 0
def dfs(lst):
    global ans
    if len(lst) == N:
        cum = 0
        for a,b,c,d in D:
            if lst[b-1] - lst[a-1] == c:
                cum += d
        ans = max(ans, cum)
        return 
    for ni in range(lst[-1], M+1):
        dfs(lst[:] + [ni])
for m in range(1, M+1):
    dfs([m])
print(ans)
