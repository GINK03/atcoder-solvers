
class Mint:
    __slots__ = ('value')
 
    def __init__(self, value=0):
        self.value = int(value) % MOD
        if self.value < 0: self.value += MOD
 
    def inverse(self):
        a, b = self.value, MOD
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        if u < 0: u += MOD
        return u
 
    def __repr__(self): return str(self.value)
    def __int__(self): return self.value
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0
 
    def __iadd__(self, other):
        self.value = (self.value + int(other)) % MOD
        return self
 
    def __add__(self, other):
        new_obj = Mint(self.value)
        new_obj += other
        return new_obj
    __radd__ = __add__
 
    def __isub__(self, other):
        self.value = (self.value - int(other)) % MOD
        if self.value < 0: self.value += MOD
        return self
 
    def __sub__(self, other):
        new_obj = Mint(self.value)
        new_obj -= other
        return new_obj
 
    def __rsub__(self, other):
        new_obj = Mint(int(other))
        new_obj -= self
        return new_obj
 
    def __imul__(self, other):
        self.value = self.value * int(other) % MOD
        return self
 
    def __mul__(self, other):
        new_obj = Mint(self.value)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__
 
    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other)
        self *= other.inverse()
        return self
 
    def __floordiv__(self, other):
        new_obj = Mint(self.value)
        new_obj //= other
        return new_obj
 
    def __rfloordiv__(self, other):
        new_obj = Mint(int(other))
        new_obj //= self
        return new_obj


import sys; sys.setrecursionlimit(10**9)
import collections
N=int(input())
*A,=map(int,input().split())

MOD = 10**9 + 7

"""
# NG
que = collections.deque([("p",1 , A[0]), ("n",1 , A[0])])
ans = 0
res = []
while que:
    t, cur, acc = que.pop()
    acc += A[cur] if t == "p" else -A[cur]
    if cur == N-1: 
        ans += acc
        ans %= MOD
    if t == "p":
        for nt in ["p", "n"]:
            if cur+1 < N:
                que.append( (nt, cur+1, acc) )
    else:
        for nt in ["p"]:
            if cur+1 < N:
                que.append( (nt, cur+1, acc) )
print(ans%MOD)
"""


dp = [[0] * N for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 0
for i in range(1, N):
    # + -> +
    dp[0][i] += dp[0][i - 1]
    # - -> +
    dp[0][i] += dp[1][i - 1]
    dp[0][i] %= MOD
    # + -> -
    dp[1][i] += dp[0][i - 1]
    dp[1][i] %= MOD

# print(*dp, sep="\n")
"""ここまでは簡単"""

ans = Mint(A[0])
ans *= (dp[0][N - 1] + dp[1][N - 1])
for i in range(1, N):
    t = Mint(0)
    """ここが難しい"""
    t += dp[1][i - 1] * dp[1][N - 1 - i]
    t += dp[0][i - 1] * dp[1][N - 1 - i]
    t += dp[1][i - 1] * dp[0][N - 1 - i]
    ans += A[i] * t
print(ans)
