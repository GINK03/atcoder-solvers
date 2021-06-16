import collections

N,M=map(int,input().split())

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

    if a == []: # 入力が1のときの例外
        a.append(1)
    return a


mod = 10 ** 9 + 7
def mod_cmb(n, a, mod):
    nca = 1
    for i in range(a):
        nca *= (n - i) * pow(a - i, mod - 2, mod)
        nca %= mod
    return nca


primes = prime_factorize(abs(N))
ans = 1
for prime, v in collections.Counter(primes).items():
    ans *= mod_cmb(v+M-1, min(M-1,v), mod)
    ans %= mod
# プラスマイナスの組み合わせ数
ans *= pow(2, M-1, mod)%mod
ans %= mod

print(ans)

