import os

n = int(input())
ax = list(map(int,input().split()))

lh,rh = 0,0

ma = 0

buff = set([ax[0]])

ans = len(buff)
while True:
    if rh+1 > len(ax)-1:
        break
    elif ax[rh+1] not in buff:
        buff.add(ax[rh+1])
        rh += 1
    else:
        buff -= {ax[lh]}
        lh += 1
    #print(buff)
    ans = max(ans, len(buff))
print(ans)
