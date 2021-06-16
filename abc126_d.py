import sys; sys.setrecursionlimit(10**9)

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    u,v,w=map(int,input().split())
    u-=1; v-=1
    G[u].append( (v,w) )
    G[v].append( (u,w) )


vis = set()
mem = dict()
def dfs(i, acc):
    if i in vis:
        return
    vis.add(i)
    mem[i] = acc
    for j, w in G[i]:
        dfs(j, acc+w)
dfs(0, 0)

for i in range(N):
    if mem[i]%2 == 0:
        print(0)
    else:
        print(1)
