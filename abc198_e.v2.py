import collections
import sys; sys.setrecursionlimit(10**9)
N = int(input())
*C, = map(int, input().split())


G = collections.defaultdict(list)
for n in range(N-1):
    A, B = map(int, input().split())
    A-=1; B-=1
    G[A].append(B)
    G[B].append(A)

vmem = set()
cmem = collections.defaultdict(int)
def dfs(i):
    if i in vmem:
        return 
    vmem.add(i)
    if cmem[C[i]] == 0:
        ans.append(i+1)
    else:
        ...
    cmem[C[i]] += 1
    for j in G[i]:
        dfs(j)
    cmem[C[i]] -= 1


ans = []
dfs(0)
ans.sort()
print(*ans, sep="\n")
