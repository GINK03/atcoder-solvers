import math

def mod_cmb(n, a, mod):
    nca = 1
    for i in range(a):
        nca *= (n - i) * pow(a - i, mod - 2, mod)
        nca %= mod
    return nca

N, A, B = map(int,input().split())
MOD=10**9+7

all = pow(2,N, MOD)-1
anum = mod_cmb(N,A,MOD)
bnum = mod_cmb(N,B,MOD)

print((all-anum-bnum)%MOD)
