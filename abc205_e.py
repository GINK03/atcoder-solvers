


MOD = 10**9 + 7
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

def paths(x: int, y: int) -> Mint:
    if (x < 0 or x < 0):
        return Mint(0)
    ret = Mint(1)
    for i in range(1, x+y+1):
        ret *= i
    for i in range(1, x+1):
        ret //= i
    for i in range(1, y+1):
        ret //= i
    return ret

N,M,K=map(int,input().split())
path1 = paths(N, M)
h = N-(K+1)
w = M+(K+1)
path2 = paths(h,w)

if N > M + K:
    print(0)
else:
    print(path1-path2)

