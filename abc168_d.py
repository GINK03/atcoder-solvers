import sys
sys.setrecursionlimit(9999)

n,m=map(int,input().split())

ps = [-1] * n
ps[0] = 0
tmps = {}
for _ in range(m):
    a,b=map(int,input().split())
    ai,bi=a-1,b-1
    if ai not in tmps:
        tmps[ai] = []
    tmps[ai].append(bi)
    if bi not in tmps:
        tmps[bi] = []
    tmps[bi].append(ai)

# print(tmps)

if 0 not in tmps:
    print("No")
    exit()


def puts(ks):
    nks = []
    for k in ks:
        _nks = tmps[k]
        for nk in _nks:
            if ps[nk] == -1:
                ps[nk] = k
                nks.append(nk)
    if nks == []:
        return None
    # puts(nks)
    return nks

ks = [0]
while True:
    nks = puts(ks)
    if nks is None:
        break
    else:
        ks = nks

#print(ps)

if -1 in ps:
    print("No")
    exit()

print("Yes")
for p in ps[1:]:
    print(p+1)

