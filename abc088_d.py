import collections
import math
H,W=map(int,input().split())
G=[list(input()) for h in range(H)]
que = collections.deque([(0,0)])
dp = [[-math.inf]*W for h in range(H)] 
dp[0][0] = 0
def bfs():
    while que:
        cur = que.popleft()
        for a,b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh = cur[0] + a
            nw = cur[1] + b
            if nh > H-1 or nh < 0 or nw < 0 or nw > W-1:
                continue
            if G[nh][nw] == "#":
                continue
            if dp[nh][nw] != -math.inf:
                continue
            dp[nh][nw] = dp[cur[0]][cur[1]] + 1
            que.append( (nh, nw) )
bfs()

white_num = sum(sum([1 for e in line if e == "."]) for line in G)
if dp[H-1][W-1] != -math.inf:
    print(white_num - dp[H-1][W-1] - 1)
else:
    print(-1)

    

