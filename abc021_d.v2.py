
MOD = 10 ** 9 + 7

mod = 10 ** 9 + 7
def mod_cmb(n, a, mod):
    nca = 1
    for i in range(a):
        nca *= (n - i) * pow(a - i, mod - 2, mod)
        nca %= mod
    return nca

N = int(input())
K = int(input())

print(mod_cmb(N+K-1, K, mod)) # 120
