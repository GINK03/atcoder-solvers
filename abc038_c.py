import os
n = int(input())
ax = list(map(int,input().split()))

lh,rh=0,0

s = ax[rh]

cp = {}
while True:
    if lh == 0 and rh == 0:
        cp[0] = 0
    if rh+1 <= len(ax)-1 and \
            s < ax[rh+1]:
        s=ax[rh+1]
        rh+=1
        cp[lh] = rh
        
    elif rh > lh:
        lh=rh
        #rh=lh
        #s=ax[rh]
    elif rh+1 <= len(ax)-1 and rh == lh:
        rh+=1
        lh+=1
        s=ax[rh]
        cp[lh] = rh
    else:
        break
    #print(s, (lh,rh))
# む・・
mm = {1:1, 0:0}
def f(x):
    if mm.get(x-1) is None:
        f(x-1)
    mm[x] = x + mm.get(x-1)
    return mm[x]
s = 0
for lh,rh in cp.items():
    #print(f(rh-lh+1), lh, rh)
    s += f(rh-lh+1)
print(s)
