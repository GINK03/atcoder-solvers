

import collections

N,M=map(int,input().split())
G = collections.defaultdict(list)

for m in range(M):
    K = int(input())
    *R,=map(int,input().split())
    for r in R:
        r -= 1
        G[(r, "V")].append( (m, "E") )
        G[(m, "E")].append( (r, "V") )

que = collections.deque([ ((0, "V"), 0)])
vis = set()
nc = dict()

while que:
    node, cnt = que.popleft()
    if node in vis:
        continue
    nc[node] = cnt
    vis.add(node)
    for nnode in G[node]:
        if nnode not in vis:
            if nnode[1] == "V":
                que.append( (nnode, cnt+1) )
            else:
                que.append( (nnode, cnt) )

for n in range(N):
    print(nc.get((n, "V"),-1))





