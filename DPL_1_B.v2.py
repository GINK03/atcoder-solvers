import collections
import itertools
import sys; sys.setrecursionlimit(10**9)
N, W = map(int, input().split())
vw = [ [list(map(int, input().split())), [0, 0]] for _ in range(N)]


mem = collections.defaultdict(lambda :-float('inf'))
for es in itertools.product(*vw):
    # print(es)
    v = sum(map(lambda x:x[0], es))
    w = sum(map(lambda x:x[1], es))
    if w <= W:
        mem[w] = max(v, mem[w])
print(max(mem.values()))

