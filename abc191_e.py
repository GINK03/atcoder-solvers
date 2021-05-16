
import collections
import heapq
import math

N,M=map(int,input().split())
G = collections.defaultdict(list)

for _ in range(M):
    u, v, c = map(int, input().split())
    G[u-1].append((v-1,c))

for n in range(N):
    dist = [math.inf for _ in range(N)]
    Q = []
    heapq.heappush(Q, (0,n)) # 距離d, 頂点iの順
    flag = True
    nums = [0]*N
    while Q:
        d, i = heapq.heappop(Q)
        # 帰り際であったら終了する
        if i == n and d > 0:
            print(d)
            flag = False
            break
        # 行き帰りで二回だからたかだか二回に限定する
        if nums[i] >= 2:
            continue
        nums[i] += 1
        for j, c in G[i]:
            # より安くなる可能性がある場合は探索し、ノードをヒープに入れる
            if dist[j] > d + c:
                dist[j] = d + c
                heapq.heappush(Q, (dist[j], j))
    if flag:
        print(-1)
