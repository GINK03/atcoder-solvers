import collections
import sys; sys.setrecursionlimit(10**9)
N,M=map(int,input().split())

G=collections.defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    a-=1;b-=1
    G[a].append(b)
    G[b].append(a)

ans = 0
def dfs(i, sts):
    global ans
    if len(sts) == N:
        ans += 1
        return
    for j in G[i]:
        if j in sts: # setのほうが軽い
            continue
        dfs(j, sts | {j})

dfs(0, {0})
print(ans)
