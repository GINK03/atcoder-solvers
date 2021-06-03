import collections
import itertools
import numpy as np
N,K=map(int,input().split())

Q = collections.defaultdict(int)
for _ in range(K):
    day,menu=map(int,input().split())
    day -= 1;
    Q[day] = menu

dp = np.zeros((N+1,4,4)).astype(int).tolist()
dp[0][0][0] = 1
MOD = 1e4

for day, want, day1, day2 in itertools.product(range(N), [0, 1,2,3], [0,1,2,3], [0,1,2,3] ):
    if not (want == day1 == day2):
        dp[day+1][want][day1] += dp[day][day1][day2]

ans = sum(dp[-1][i][j] for i in range(4) for j in range(4)) % MOD
print(ans)
