
import collections
import heapq
import sys; sys.setrecursionlimit(10**9)
N = int(input())
G = collections.defaultdict(lambda :[])

for n in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
for n in range(N):
    G[n].sort()

vis = set()
trc = []
def dfs(i):
    vis.add(i)
    trc.append(i+1)
    for j in G[i]:
        if j in vis:
            continue
        dfs(j)
        trc.append(i+1)

dfs(0)
print(*trc)
