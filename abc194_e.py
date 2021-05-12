import collections
import math
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))


b = collections.defaultdict(int)
for i in range(M):
    if A[i] < M:
        b[A[i]] += 1


ans = [M]
heapq.heapify(ans)
for m in range(N):
    if b[m] == 0:
        heapq.heappush(ans, m)
        break


to_print = ans[0]
for n in range(M, N):
    if A[n] < M:
        b[A[n]] += 1
    if n > M - 1:
        b[A[n]] += 1
        if A[n - M] < M and b[A[n - M]] > 0:
            b[A[n - M]] -= 1
            if b[A[n - M]] == 0:
                heapq.heappush(ans, A[n - M])
    mex = ans[0]
    to_print = min(mex, to_print)

print(to_print)
