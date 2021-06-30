import collections

N = int(input())
G = [[] for _ in range(N+1)]


que = collections.deque([])
vis = set()
for i in range(1, N+1):
    a, b = map(int,input().split())
    G[a].append(i)
    G[b].append(i)
    if a == i or b == i:
        vis.add(i)
        que.append(i)


trc = []
while que:
    pos = que.pop()
    trc.append(pos)

    for i in G[pos]:
        if i in vis:
            continue
        vis.add(i)
        que.append(i)

trc = trc[::-1]

if len(trc) != N:
    print(-1)
else:
    print(*trc, sep="\n")

