import math
N,M,Q=map(int,input().split())

WV=[]
for _ in range(N):
    W,V=map(int,input().split())
    WV.append((W,V))
Xs=list(map(int,input().split()))
# 貪欲法で最大のVから空いている最小の箱に入れていく
WV.sort(key=lambda x:-x[1])

for _ in range(Q):
    L,R=map(int,input().split())
    useful = Xs[:L-1] + Xs[R:]
    useful.sort()
    #print(L,R,useful)
    vals = 0
    for w,v in WV:
        for i in range(len(useful)):
            if w <= useful[i]:
                vals += v
                useful[i]=-math.inf
                break
    print(vals)



