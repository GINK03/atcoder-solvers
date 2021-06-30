

N = int(input())

LR = []
for n in range(N):
    l,r=map(int,input().split())
    LR.append( (l,r) )

import itertools

exps = 0
for (l0, r0), (l1, r1) in itertools.combinations(LR, 2):
    is_tenchi = 0
    total = 0
    for i in range(l0, r0+1):
        for j in range(l1, r1+1):
            if i > j:
                is_tenchi += 1
            total += 1
    exps += is_tenchi / total
print(exps)

