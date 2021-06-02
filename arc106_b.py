
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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
        if x == y:
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

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
import collections
# import numpy as np

uf = UnionFind(N)
for _ in range(M):
    c,d = map(int,input().split())
    c-=1; d-=1
    uf.union(c,d)
import itertools
import statistics
cls = [(uf.find(n), n) for n in range(N)]
cls.sort()
cls = {k:list(map(lambda x:x[1], v)) for k, v in itertools.groupby(cls, key=lambda x:x[0])}
nums = set(cls.keys())

checks = []
for num in nums:
    a = statistics.mean([A[ai] for ai in cls[num]])
    b = statistics.mean([B[ai] for ai in cls[num]])
    checks.append( abs(a - b)  < 1/(10**6))
if all(checks):
    print("Yes")
else:
    print("No")
