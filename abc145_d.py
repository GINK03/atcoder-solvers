
MOD=10**9+7
N=10**6
class Wrap():
    def __init__(self):
        self.fact = [1, 1]  # fact[n] = (n! mod p)
        self.factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
        self.inv = [0, 1]  # factinv 計算用
        for i in range(2, N + 1):
            self.fact.append((self.fact[-1] * i) % MOD)
            self.inv.append((-self.inv[MOD % i] * (MOD // i)) % MOD)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % MOD)
    def cmb(self, n, r):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n-r] % MOD
wrap = Wrap()

X,Y=map(int,input().split())

if X == 0 or Y == 0:
    print(0)
    exit()
if max(X,Y)/min(X,Y) > 2:
    print(0)
    exit()
if (X+Y)%3 != 0:
    print(0)
    exit()
print(wrap.cmb((X+Y)//3,X-(X+Y)//3))


