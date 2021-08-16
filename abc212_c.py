
N, M = map(int, input().split())

*A, = map(int, input().split())
A = [(a, "A") for a in A]
*B, = map(int, input().split())
B = [(b, "B") for b in B]

X = A + B
X.sort()

ans = float("inf")
for i in range(N+M-1):
    if X[i+1][1] != X[i][1]:
        ans = min(ans, X[i+1][0] - X[i][0])
print(ans)
