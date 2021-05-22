
import heapq



def dijkstra(s, t, G):
    dist = [float('inf') for _ in range(N)]
    dist[s] = 0
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (0,s)) # 距離d, 頂点iの順
    done = [False for _ in range(N)]
    while que:
        d, i = heapq.heappop(que)
        # すでに訪れたところは処理しない
        if done[i]:
            continue
        done[i] = True
        for j, c in sorted(G[i]):
            # 評価が未知のエッジ or より安くなる可能性がある場合は探索し、結果をヒープに入れる
            if dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(que, (dist[j], j))
    #print(G)
    print(dist[t] if dist[t] != float('inf') else -1)

N, K = map(int, input().split())
G = [[] for _ in range(N)]
Q = []
for _ in range(K):
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        a, s, t = lst
        s-=1
        t-=1
        dijkstra(s,t,G)
    else:
        a, s, t, w = lst
        s-=1
        t-=1
        G[s].append((t, w))
        G[t].append((s, w))
