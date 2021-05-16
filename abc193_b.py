import math
N=int(input())

ans = []
for _ in range(N):
    A,P,X=map(int,input().split())
    X-=math.ceil(A-0.5)
    if X > 0:
        ans.append(P)

if ans:
    print(min(ans))
else:
    print(-1)

