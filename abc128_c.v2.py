N,M = map(int,input().split())

B = []
for m in range(M):
    lst = list(map(int,input().split()))
    k=lst.pop(0)
    switch=[s-1 for s in lst]
    B.append(switch)

Ps=list(map(int, input().split()))


cnt = 0
P = 1<<N
for i in range(P):
    switch = [0]*N
    for j in range(N):
        if i&(1<<j) > 0:
            switch[j] = 1
        else:
            pass
    ons = []
    for m in range(M):
        if sum([switch[s] for s in B[m]])%2 == Ps[m]:
            # on
            ons.append(True)
        else:
            ons.append(False)
    if all(ons):
        cnt += 1
    #print(f"{i:0b}", ons)
print(cnt)
