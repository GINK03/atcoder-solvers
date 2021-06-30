

N = int(input())
*A,=map(int,input().split())

S = sum(A)
x0 = S - 2*sum([A[i] for i in range(1, N-1, 2)])
x = [x0]
for i in range(N-1):
    x1 = 2*A[i] - x[-1]
    x.append(x1)
print(*x)
