
MOD = 10**9 + 7
import collections
N=int(input())
*A,=list(input())

ans = 1
for v in collections.Counter(A).values():
    ans *= (v+1)
    ans %= MOD
ans -= 1
print(ans%MOD)

