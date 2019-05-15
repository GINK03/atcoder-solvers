H,W = map(int,input().split())

S = [['x']*W]*H

for h in range(H):
    S[h] = list(input())
#print(S)

def pmap(func):
    return func()
def hmap():
    for h in range(H):
        bw, sw = 0,0
        for i in range(W):
            if S[h][i] != '#' and i != W-1:
                bw += 1
            elif S[h][i] == '#':
                for asw in range(sw, i):
                    S[h][asw] = bw
                bw = 0
                sw = i+1
                #print(sw,bw)
            elif i == W-1:
                bw += 1
                #print('err')
                for asw in range(sw, W):
                    S[h][asw] = bw
    return S
#print('2nd')
#print(S)
def wmap():
    for w in range(W):
        bh, sh = 0,0
        for i in range(H):
            if S[i][w] != '#' and i != H-1:
                bh += 1
            elif S[i][w] == '#':
                for ash in range(sh, i):
                    S[ash][w] = bh
                bh = 0
                sh = i+1
                #print(sh,bh)
            elif i == H-1:
                bh += 1
                #print('err')
                for ash in range(sh, H):
                    S[ash][w] = bh
    return S
#print(S)
import itertools
from concurrent.futures import ProcessPoolExecutor as PPE
with PPE(max_workers=2) as exe:
    Ss = []
    for aS in exe.map(pmap, [hmap, wmap]):
        Ss.append(list(itertools.chain.from_iterable(aS)))
r = 0
for s1, s2 in zip(Ss[0], Ss[1]):
    if str(s1).isdecimal():
        r = max(r, s1 + s2)
print(r-1)
