
import collections

inf = float("inf")
N = int(input())

A = []
for n in range(N):
    x, y = map(int, input().split())
    A.append( (x, y) )
A.sort()

def f(k):
    left = N - 1
    mi, ma = inf, -inf
    res = 0
    for x, y in A[::-1]:
        while left >= 0 and x + k <= A[left][0]:
            mi = min(mi, A[left][1])
            ma = max(ma, A[left][1])
            left -= 1
        res = max(res, y - mi, ma - y)
    return res >= k

ok, ng = 0, 10**9 + 7
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)
