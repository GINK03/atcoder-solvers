import os

n,k_=map(int,input().split())
px=[(i+1,x) for i,x in enumerate(map(int,input().split()))]
cx=list(map(int,input().split()))

tmp = []
for p in px:

    is_ok = False
    print(p, tmp)
    for t in tmp:
        if p[1] == t[0]:
            if p[0] != t[-1]:
                t.insert(0, p[0])
            is_ok = True
        elif p[0] == t[-1]:
            if p[1] != t[0]:
                t.append(p[1])
            is_ok = True 
    if is_ok ==False:
        tmp.append(list(p))

import copy
print(tmp)
    
for t in tmp:
    cir = [cx[ti-1] for ti in t*2]
    ep = []
    for i in range(len(cir)+1):
        for k in range(i+1, len(cir)+1):
            if k-i > k_:
                continue
            ep.append([k-i, sum(cir[i:k])])

    print(cir, ep)
