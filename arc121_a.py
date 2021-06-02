

N=int(input())

XY = []
for i in range(N):
    x,y = map(int, input().split())
    XY.append( (x, y, i) )
XY.sort()

#print(XY)

a = XY[:2] + XY[-2:]
XY.sort(key=lambda x:x[1])
a += XY[:2] + XY[-2:]

a = list(set(a))

import itertools
##print(a)

cds = []
for c0, c1 in itertools.combinations(a, 2):
    cd = max(abs(c0[0] - c1[0]), abs(c0[1] - c1[1]))
    cds.append(cd)
cds.sort()
print(cds[-2])
