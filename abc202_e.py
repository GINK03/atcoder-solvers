import sys
import bisect
sys.setrecursionlimit(10**8)
import collections

N=int(input())
P=list(map(lambda x:int(x),input().split()))
G= collections.defaultdict(list)
#G[1].append(1)
for to, frm in enumerate(P,2):
    G[frm].append(to)
    #G[to].append(frm)


Q=int(input())
UD =[] 
for _ in range(Q):
    u,d=map(int,input().split())
    UD.append( (u,d) )

vs = set()
ins = collections.defaultdict(int)
outs = collections.defaultdict(int)
depth_in = collections.defaultdict(list)

que = collections.deque([1])

cnt = 0
def dfs(i, depth):
    global cnt
    if i in vs:
        # outs[i] = cnt
        return
    vs.add(i)
    cnt += 1
    ins[i] = cnt
    depth_in[depth].append(cnt)
    for j in G[i]:
        dfs(j, depth+1)
    cnt += 1
    outs[i] = cnt
dfs(1, 0)
# print(ins)
# print(outs)

for u, d in UD:
    in_ = ins[u]
    out_ = outs[u]
    print(bisect.bisect_left(depth_in[d], out_) -  bisect.bisect_left(depth_in[d], in_))
