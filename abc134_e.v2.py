
import bisect
N=int(input())
A=[]
for _ in range(N):
    A.append(int(input()))
dp = [float("inf")]*(N+1)
dp[0] = -1
B = [1/(a+1) for a in A]
for a in B:
    # 広義単調減少
    # 以下の処理は広義単調の数を求める
    idx = bisect.bisect(dp, a)
    dp[idx] = min(a, dp[idx])

dp.pop(0)

if dp[-1] != float("inf"):
    print(N)
else:
    print(sum(1 for x in dp if x < float("inf")))
