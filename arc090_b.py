
class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        # 各親要素の番号を格納 rootの場合は、そのグループの要素数
        self.parents = [-1] * n
        self.diff_weight = [0] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # 根を見つけると同時に、他の要素の親を根に変更(経路圧縮)
            r = self.find(self.parents[x])
            # 親を遡りながら、重みの累積和を取る
            self.diff_weight[x] += self.diff_weight[self.parents[x]]
            self.parents[x] = r
            return self.parents[x]
    def weight(self, x):
        self.find(x) # 経路圧縮
        return self.diff_weight[x]
    def diff(self, x, y):
        return self.weight(y) - self.weight(x)
    def union(self, x, y, w):
        # xとyそれぞれについて、rootとの重み差分を補正
        w += self.weight(x)
        w -= self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
            w = -w
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        # x が y の親になるので、x と y の差分を diff_weight[y] に記録
        self.diff_weight[y] = w
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N,M=map(int,input().split())
wuf = WeightedUnionFind(n=N)
for _ in range(M):
    l, r, d = map(int,input().split())
    l-=1; r-=1;
    if wuf.same(l, r):
        if wuf.diff(l,r) != d:
            print("No")
            exit()
    else:
        wuf.union(l, r, d)
print("Yes")
