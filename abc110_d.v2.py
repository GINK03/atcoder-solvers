
N, M = map(int,input().split())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

fs = prime_factorize(M)

mod = 10 ** 9 + 7
def mod_cmb(n, a, mod):
    nca = 1
    for i in range(a):
        nca *= (n - i) * pow(a - i, mod - 2, mod)
        nca %= mod
    return nca

from collections import Counter
c = dict(Counter(fs))

ans = 1
for fact in c:
  freq = c[fact]
  ans *= mod_cmb(N+freq-1,freq, mod) 
print(ans%((10**9)+7))
