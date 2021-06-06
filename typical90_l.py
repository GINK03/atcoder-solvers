
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


H,W=map(int,input().split())
ufind = UnionFind(n=H*W)

G=[["w"]*W for _ in range(H)]
Q=int(input())

for _ in range(Q):
    q = input()
    if q[0] == "1":
        _, h,w=map(int,q.split())
        h-=1;w-=1
        G[h][w] = "r"
        for dh, dw in [(1,0), (-1,0), (0, 1), (0, -1)]:
            nh,nw=h+dh,w+dw
            if not(0 <= nh < H and 0 <= nw < W):
                continue
            if G[nh][nw] == "r":
                ufind.union(h*W+w, nh*W+nw)
    else:
        _, h0,w0, h1, w1 = map(int,q.split())
        h0-=1;w0-=1; h1-=1; w1-=1
        if G[h0][w0] == "w" or G[h1][w1] == "w":
            print("No")
            continue

        if ufind.find(h0*W + w0) != ufind.find(h1*W+w1):
            print("No")
        else:
            print("Yes")
        
