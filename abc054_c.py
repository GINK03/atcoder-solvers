import collections
import itertools
import copy
N,M=map(int,input().split())


G=collections.defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    a-=1;b-=1

    G[a].append(b)
    G[b].append(a)

que = collections.deque([[0, []]])

ans = 0
while que:
    i, memo = que.pop()
    if i in memo:
        continue
    memo.append(i)
    if len(memo) == N:
        ans += 1
        continue
    for j in G[i]:
        que.append( (j, copy.copy(memo)) )

print(ans)
