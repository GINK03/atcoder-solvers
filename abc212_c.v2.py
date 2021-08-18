import bisect
N, M = map(int, input().split())
*A,=map(int, input().split())
*B,=map(int, input().split())
A.sort()
A = [-float("inf")] + A + [float("inf")]

ans = float("inf")
for b in B:
    i = bisect.bisect_left(A, b)
    ans = min(ans, abs(A[i]-b), abs(A[i-1]-b))
print(ans)
