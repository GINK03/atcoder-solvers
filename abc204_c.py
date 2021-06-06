
import math

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(0, M):
    u, v = map(int, input().split())
    u-=1; v-=1
    G[u].append(v)


import collections

def dfs(si, arg):
    vis = collections.defaultdict(int)
    que = collections.deque([si])
    while que:
        i = que.pop()
        if vis[i] >= 1:
            continue
        vis[i] += 1
        for j in G[i]:
            que.append( j )
    # print(si, vis)
    return len(vis)

ans = 0
for n in range(N):
    n = dfs(n, [])
    ans += n
print(ans)
