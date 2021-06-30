import collections


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.has_cycles = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # 積極的aggregation
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 同じノード同士ならばなにもしない
        # ここに閉路情報を入れることができる
        if x == y:
            self.has_cycles[x] = 1
            return
        # 既知の親子で小さいものが左に来るべき
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        # rootノードを負の値で参照量をカウントしたいため、このような+=が入っている
        self.parents[x] += self.parents[y]
        # rootノードでなければ、正のindex値を入れる
        self.parents[y] = x

    def size(self, x):
        # rootノードの参照料を保存したものを取り出している
        return -self.parents[self.find(x)]

    def same(self, x, y):
        # 同じルートを持つか
        return self.find(x) == self.find(y)

    def roots(self):
        # どのノードがrootとなるか
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        # グループの個数
        return len(self.roots())

    def all_group_members(self) -> "Tuple[GroupMember, GroupCycle]":
        # rootをkeyに子をvalueのlistに, 閉路情報も返す
        group_members = collections.defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        group_cycle = collections.defaultdict(bool)
        for group, members in group_members.items():
            group_cycle[group] = True if any([self.has_cycles[member] for member in members]) else False
        return group_members, group_cycle


N, M = map(int, input().split())

AB = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB.append((a, b))


uf = UnionFind(n=N)
ans = [0] # すべて崩落するので初期値は0でよい
for a,b in AB[::-1]:
    if uf.find(a) == uf.find(b):
        tmp = ans[-1]
    else:
        tmp = ans[-1] + uf.size(a)*uf.size(b)
    ans.append(tmp)
    uf.union(a,b)

ans.pop()
max_ = N*(N-1)//2
print(*[max_ -x for x in ans[::-1]], sep="\n")

