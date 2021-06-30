import bisect
import math
from scipy.special import comb

N = int(input())
*A,=map(int,input().split())
A.sort()

max_a = A[-1]

mid = max_a / 2

idx = bisect.bisect_left(A, mid) # 半分以下の点を探す

m1 = A[idx]
m2 = A[idx-1] # 次がこれ

if min(max_a - m1, m1) > min(max_a - m2, m2):
    print(max_a, m1)
else:
    print(max_a, m2)

