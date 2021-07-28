
N=int(input())

ans = 0
for A in range(1, N):
    B = (N-1)//A 
    ans += B

print(ans)
