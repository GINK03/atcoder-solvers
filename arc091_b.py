
N,K =map(int,input().split())

if K == 0:
    print(N*N); exit()

ans = 0
for b in range(K+1, N+1):
    ans += N//b * (b-K)
    ans += max(N%b - K + 1, 0)
print(ans)

