

N=int(input())
*X,=map(int,input().split())

C = sorted(X)
m0 = C[N//2-1]
m1 = C[N//2]

for i in range(N):
    if X[i]<=m0:
        print(m1)
    else:
        print(m0)

