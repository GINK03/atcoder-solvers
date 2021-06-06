
class Segtree:
    n = 1
    size = 1
    log = 2
    d = [0]
    op = None
    e = 10 ** 15
    def __init__(self, V: "List", OP: "function", E: "基底"):
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)
    def set(self, p, x): # 1
        assert 0 <= p and p < self.n
        p += self.size
        self.d[p] = x
        [self.update(p >> i) for i in range(1, self.log + 1)]
    def get(self, p): # 2
        assert 0 <= p and p < self.n
        return self.d[p + self.size]
    def prod(self, l, r): # 3
        assert 0 <= l and l <= r and r <= self.n
        sml = smr = self.e
        l += self.size; r += self.size
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                smr = self.op(self.d[r - 1], smr)
                r -= 1
            l >>= 1; r >>= 1
        return self.op(sml, smr)
    def all_prod(self): # 4
        return self.d[1]
    def max_right(self, l, f): # 5
        assert 0 <= l and l <= self.n
        assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size
        sm = self.e
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not (f(self.op(sm, self.d[l]))):
                while l < self.size:
                    l = 2 * l
                    if f(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n
    def min_left(self, r, f): # 6
        assert 0 <= r and r < self.n
        assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm = self.e
        while 1:
            r -= 1
            while r > 1 & (r % 2):
                r >>= 1
            if not (f(self.op(self.d[r], sm))):
                while r < self.size:
                    r = 2 * r + 1
                    if f(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                break
        return 0
    def update(self, k): # 7
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

N = int(input())
S = input()

class E:
    def __init__(self, e, w):
        self.E = e
        self.W = w
    def __add__(self, other):
        return E(e=self.E + other.E, w=self.W+other.W)
    def __repr__(self):
        return f"E={self.E}, W={self.W}"
e = E(0, 0)
A = [E(e=0, w=1) if s == "W" else E(e=1, w=0) for s in S]
OP = lambda x,y:x+y
stree = Segtree(V=A, OP=OP, E=e )
ans = float('inf')
for i in range(N):
    right = stree.prod(i+1, N)
    left = stree.prod(0, i)
    ans = min(ans, right.E + left.W)
print(ans)


