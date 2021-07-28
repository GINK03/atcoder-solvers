
N, x = map(int,input().split())
*A,=map(int,input().split())
c = 0
if A[0] > x:
    tmp = A[0] - x
    A[0] = x
    c += tmp
for i in range(1, N):
    if A[i] + A[i-1] > x:
        tmp = (A[i] + A[i-1]) - x
        A[i] -= tmp
        c += tmp
print(c)
