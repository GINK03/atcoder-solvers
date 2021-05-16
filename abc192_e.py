
import collections
import heapq
import math

N,M,X,Y=map(int,input().split())
X-=1
Y-=1

G = collections.defaultdict(list)

for _ in range(M):
    A,B,T,K = map(int, input().split())
    G[A-1].append((B-1,T,K))
    G[B-1].append((A-1,T,K))

cost = [math.inf for _ in range(N)]
que = []
heapq.heapify(que)
heapq.heappush(que, (0, X)) # コスト
nums = [0]*N
while que:
    '''
    ac: accumlated cost
    nc: next cost
    '''
    ac, i = heapq.heappop(que)
    if ac > cost[i]:
        continue
    cost[i] = ac

    for j, t, k in G[i]:
        nc = ac
        if ac%k != 0:
            nc += k - ac%k
        nc += t
        heapq.heappush(que, (nc, j))

if cost[Y] is math.inf:
    print(-1)
else:
    print(cost[Y])
#print(dist)
