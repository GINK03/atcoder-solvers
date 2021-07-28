

N, Q = map(int,input().split())

G = [[] for n in range(N)]
for n in range(N-1):
    a,b = map(int,input().split())
    a-=1; b-=1
    G[a].append(b)
    G[b].append(a)

import collections

que = collections.deque([(0, 0)])

vis = dict()


while que:
    i, cnt = que.pop()
    vis[i] = cnt
    if cnt == 1:
        cnt = 0
    else:
        cnt = 1
    for j in G[i]:
        if j in vis:
            continue
        que.append((j, cnt))

for q in range(Q):
    c,d = map(int,input().split())
    c-=1; d-=1
    #print("d", vis[c], vis[d])
    if (vis[c]+vis[d])%2 == 0:
        print("Town")
    else:
        print("Road")
