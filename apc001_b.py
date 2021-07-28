import math
N = int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())

diff = sum(B) - sum(A)

if diff < 0:
    print("No")
    exit()


min_ops = 0
for i in range(N):
    a,b = A[i], B[i]
    if b > a:
        min_ops += math.ceil((b - a)/2)

if min_ops > diff:
    print("No")
else:
    print("Yes")
