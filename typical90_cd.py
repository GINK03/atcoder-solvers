
MOD = 10**9 + 7

L,R=map(int,input().split())

POW10 = [0]*22
POW10[0] = 1
for i in range(1, 20):
    POW10[i] = POW10[i-1]*10

def f(x):
    if x%2 == 0:
        v1 = (x//2) % MOD
        v2 = (x+1) % MOD
        return (v1 * v2) % MOD
    else:
        v1 = ((x+1)//2) % MOD
        v2 = x % MOD
        return (v1 * v2) % MOD


ans = 0
for i in range(20):
    vl = max(L, POW10[i-1])
    vr = min(R, POW10[i] - 1)

    if vl > vr:
        continue
    val = (f(vr) - f(vl - 1) + MOD) % MOD
    ans += i * val
    ans %= MOD

print(ans)
