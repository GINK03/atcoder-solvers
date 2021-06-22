
import collections
import sys; sys.setrecursionlimit(10**9)
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
        return group_members


N=int(input())
*A,=map(int,input().split())

if N%2 == 1:
    L, R = A[:N//2], A[N//2+1:]
else:
    L, R = A[:N//2], A[N//2:]

if N == 1:
    print(0)
    exit()
# print(L,R)

RR = R[::-1]

uf = UnionFind(n=2*(10**5) + 10)
for i in range(len(L)):
    if L[i] != RR[i]:
        uf.union( L[i], RR[i] )
# print(rec)
gm = uf.all_group_members()
# print(gm)
ans = 0
for k, v in gm.items():
    if len(v) >= 1:
        ans += len(v) - 1
print(ans)




