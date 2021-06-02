# 2021/05/30
# かなり難しい気がする

import math
import itertools

# 桁dpを構築
# https://gink03.github.io/digit-dp-charactor/
dp = [[0]*31 for _ in range(31)]
dp[0][0] = 1

for a, b in itertools.product(range(31), range(31)):
    if a > 0:
        dp[a][b] += dp[a-1][b] 
    if b > 0:
        dp[a][b] += dp[a][b-1]

def rec(a, b, k):
    if a == 0:
        return "b"*b
    if b == 0:
        return "a"*a
    if k <= dp[a-1][b]:
        return "a" + rec(a-1, b, k)
    else:
        return "b" + rec(a, b-1, k-dp[a-1][b])


A,B,K=map(int,input().split())

print(rec(A,B,K))
