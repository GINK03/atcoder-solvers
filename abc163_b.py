N,M=map(int,input().split())
A=list(map(int,input().split()))


a=N-sum(A)
if a < 0:
    print(-1)
else:
    print(a)
