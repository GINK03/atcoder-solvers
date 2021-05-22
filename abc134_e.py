
N=int(input())
A=[]
for _ in range(N):
    A.append(int(input()))
import bisect
dp = [-1]*(N)
for a in A:
    # 広義単調減少
    # 以下の処理は広義単調の数を求める
    idx = bisect.bisect_left(dp, a)
    dp[idx-1] = a
print(dp)
print(N-bisect.bisect_left(dp,0))
