
import collections

N,Q=map(int,input().split())

G=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)


P=[0]*N
for _ in range(Q):
    p,x=map(int,input().split())
    P[p-1]+=x
que = collections.deque([0])
parents = collections.defaultdict(set)
while que:
    i = que.pop()
    for j in G[i]:
        if i in parents[j]:
            continue
        parents[j].add(i)
        P[j] += P[i]
        que.append( j )
print(*P)



