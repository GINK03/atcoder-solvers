import collections
N=int(input())

L=collections.defaultdict(list)
for n in range(N):
    A = int(input())
    for _ in range(A):
        x,y=map(int,input().split())
        x-=1
        L[n].append( (x,y) )

Pat = 1 << N

ans = 0
for i in range(Pat):
    tmp = []
    for j in range(N):
        if i&(1<<j) > 0:
            tmp.append(1)
        else:
            tmp.append(0)

    res = True
    for j in range(N):
        if i&(1<<j) == 0:
            continue
        for x, y in L[j]:
            if tmp[x] == y:
                pass
            else:
                res = False
                break   
    #print(bin(i), res)
    if res:
        ans = max(ans, bin(i).count('1'))
print(ans)
