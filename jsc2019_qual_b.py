
N,K=map(int,input().split())
*A,=map(int,input().split())
MOD = 10**9 + 7

by = (K * (K - 1) // 2) % MOD

ans = 0
for i, a in enumerate(A):
    x = 0
    y = 0
    for j, b in enumerate(A):
        if a > b:
            x += 1
            if i < j:
                y += 1
    ans += y * K
    ans %= MOD
 
    ans += x * by
    ans %= MOD
 
print(ans)
