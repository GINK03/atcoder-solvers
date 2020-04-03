N, B, R = map(int,input().split())

rate = N//(B+R)

m = 0
N %= (R+B)
if N!=0:
    if B >= N:
        m = N
    else:
        m = B
ans = rate * B + m
print(ans)
