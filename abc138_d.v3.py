
import collections
import sys; sys.setrecursionlimit(10**9)
N,Q=map(int,input().split())

G = [[] for _ in range(N)]

for _ in range(N-1):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].append(b)
    G[b].append(a)

PX = [0]*N
for _ in range(Q):
    p,x=map(int,input().split())
    p-=1
    PX[p] += x

X = [0]*N
vis = set()
"""
def dfs(i, cum):
    if i in vis:
        return 
    vis.add(i)
    X[i] = cum
    for j in G[i]:
        dfs(j, cum+PX[j])
"""
def dfs(i, cum):
    que = collections.deque([(i, cum)])
    while que:
        i, cum = que.pop()
        if i in vis:
            continue
        vis.add(i)
        X[i] = cum
        for j in G[i]:
            que.append( (j, cum+PX[j]) )


dfs(0, PX[0])

print(*X)
