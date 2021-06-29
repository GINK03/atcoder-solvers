

N=int(input())

LRT = []
for _ in range(N):
    t, l, r = map(int,input().split())
    if t == 1:
        l=l; r=r
    elif t == 2:
        l=l; r-=0.1
    elif t == 3:
        l+=0.1; r=r
    elif t ==4:
        l+=0.1; r-=0.1
    LRT.append( (l, r, t) )

tmp = set()
for i in range(N):
    l, r, t = LRT[i]
    for j in range(N):
        l2, r2, t2 = LRT[j]
        if i == j:
            continue
        cnt = 0
        if l2 <= l <= r2:
            cnt = 1
        if l2 <= r <= r2:
            cnt = 1
        if cnt:
            if i > j:
                tmp.add( (j, i) )
            else:
                tmp.add( (i, j))
print(len(tmp))

        

