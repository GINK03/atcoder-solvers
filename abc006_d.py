
import bisect

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

INF = float('inf')
dp = [INF]*(N+1)
dp[0] = -1
for a in A:
    idx = bisect.bisect(dp, a-1) # 最長増加部分列
    # idx = bisect.bisect(dp, a) # 広義最長増加部分列
    dp[idx] = min(a, dp[idx])

#print(dp)
ans = max(i for i in range(N+1) if dp[i] < INF)
print(N-ans)
