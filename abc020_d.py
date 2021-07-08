MOD = 10 ** 9 + 7

def factors(a):
    if a <= 0: return [0]
    dd0, dd1 = [], []
    for d in range(1, a+1):
        if d*d > a: break
        if a%d: continue
        dd0.append(d)
        dd1.append(a//d)
    if dd0[-1] == dd1[-1]: dd1.pop()
    return dd0+dd1[::-1]

N, K = map(int, input().split())
dd = factors(K)
M = len(dd)
dp = [0] * M

for i in range(M)[::-1]:
    d = dd[i]
    c = N // d
    dp[i] = c * (c + 1) // 2 * K % MOD
    for j in range(i + 1, M):
        if dd[j] % d == 0:
            r = dd[j] // d
            dp[i] -= dp[j] * r
            dp[i] %= MOD

ans = 0
for v in dp:
    ans += v
    ans %= MOD
print(ans)
