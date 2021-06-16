import bisect
N=int(input())

WH=[]
for _ in range(N):
    WH.append(list(map(int,input().split())))

WH = [(w,-h, h) for w,h in WH]
WH.sort()

A = [wh[2] for wh in WH]

INF = float('inf')
dp = [INF]*(N+1)
dp[0] = -1
for a in A:
    idx = bisect.bisect(dp, a-1) # 最長増加部分列
    dp[idx] = min(a, dp[idx])

ans = max(i for i in range(N+1) if dp[i] < INF)
print(ans)
