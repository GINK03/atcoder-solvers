import itertools
N=int(input())

SIZE=1001
G=[ [0]*SIZE for _ in range(SIZE) ]

for _ in range(N):
    lx,ly,rx,ry=map(int,input().split())
    G[lx][ly]+=1
    G[lx][ry]-=1
    G[rx][ly]-=1
    G[rx][ry]+=1

for x in range(SIZE):
    *tmp, = itertools.accumulate(G[x]) 
    G[x] = tmp

for y in range(SIZE):
    *tmp, = itertools.accumulate([G[x][y] for x in range(SIZE)]) 
    for xi in range(SIZE):
        G[xi][y] = tmp[xi]

# import numpy as np
# print(np.array(G))
import collections

cnt = collections.defaultdict(int)
for g in G:
    for a in g:
        cnt[a]+=1

for i in range(1,N+1):
    print(cnt[i])
