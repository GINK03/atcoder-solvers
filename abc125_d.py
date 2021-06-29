import collections

N = int(input())
*A,=map(int,input().split())

dp = collections.defaultdict(lambda :0)
dp[(0, 0)] = 0
dp[(0, 1)] = -float("inf")
for i in range(N):
    a = A[i]
    dp[(i+1, 0)] = max(dp[(i, 0)] + a, dp[(i, 1)] - a)
    dp[(i+1, 1)] = max(dp[(i, 1)] + a, dp[(i, 0)] - a)

print(dp[(N, 0)])
