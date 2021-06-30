import bisect
import math
from scipy.special import comb

N = int(input())
*A,=map(int,input().split())
A.sort()

max_a = A.pop()

mid = max_a / 2

idx = min(bisect.bisect_left(A, mid), len(A)-1)

m1 = A[idx]
m2 = A[idx-1]

if min(max_a - m1, m1) > min(max_a - m2, m2):
    print(max_a, m1)
else:
    print(max_a, m2)

