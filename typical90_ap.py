
import itertools
import numpy as np

MOD = 10**9 + 7

K = int(input())

if K%9 != 0:
    print(0)
    exit()

dp = [0] * (K+1)
dp[0] = 1
for i in range(len(dp)):
    b = min(i, 9)
    for j in range(1, b+1):
        dp[i] += dp[i-j]
        dp[i] %= MOD

print(dp[K])
