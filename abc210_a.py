
N,A,X,Y=map(int,input().split())

ans = 0

d = N-A
if d > 0:
    ans += d*Y + A*X
else:
    ans += N*X

print(ans)
