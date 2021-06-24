import collections
from dataclasses import dataclass

N,K=map(int,input().split())
*A,=map(int,input().split())
A = [a-1 for a in A]

@dataclass
class Entry:
    val: int = 0
    freq: int = 0

rec = collections.defaultdict(lambda : Entry())
cnt = 0; cur = 0; rec[cur].freq += 1
for i in range(10**18):
    nc = A[cur]
    if rec[nc].freq < 2:
        cnt += 1
        rec[nc].val = cnt
        rec[nc].freq += 1
    else:
        break
    cur = nc

head = [v+1 for v, lst in rec.items() if lst.freq <= 1]
cycle = [(v, lst.val) for v, lst in rec.items() if lst.freq == 2]
cycle.sort(key=lambda x:x[1])
cycle = [v+1 for v,r in cycle]

if len(head) > K:
    print(head[K])
else:
    K -= len(head)
    i = K%len(cycle)
    print(cycle[i])
