

N=int(input())
*P,=map(int,input().split())

X=[P[i] for i in range(N)]



cnt = 0
for i in range(N-1):
    if X[i] == i+1:
        X[i], X[i+1] = X[i+1], X[i]
        cnt += 1
if X[-1] == N:
    X[i], X[i+1] = X[i+1], X[i]
    cnt += 1

print(cnt)


