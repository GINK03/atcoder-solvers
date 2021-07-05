import collections
import math
import heapq
X,Y,A,B=map(int,input().split())

"""
二段階で考える
 1. 掛け算が有利な状況
 2. 足し算が有利な状況
"""
cnt = 0
while True:
    if X*A > X + B or X*A >= Y:
        break
    cnt += 1
    X *= A

cnt += (Y-X-1) // B
print(cnt)


