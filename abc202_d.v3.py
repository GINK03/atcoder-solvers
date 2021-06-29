# 2021/06/24
# 難しい気がする

import math
import itertools
import collections
# 桁dpを構築
# https://gink03.github.io/digit-dp-charactor/
dp = collections.defaultdict(int)
dp[(0,0)] = 1

for a, b in itertools.product(range(31), range(31)):
    dp[(a+1, b)] += dp[(a,b)]
    dp[(a,b+1)] += dp[(a,b)]

def dfs(a, b, k):
    if a == 0:
        return "b"*b
    elif b == 0:
        return "a"*a
    elif k <= dp[(a-1, b)]:
        return "a" + dfs(a-1, b, k)
    else:
        return "b" + dfs(a, b-1, k-dp[(a-1,b)])

A,B,K=map(int,input().split())
print(dfs(A,B,K))
