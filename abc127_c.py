
N,M=map(int,input().split())

agg = None
for m in range(M):
    L,R=map(int,input().split())
    if agg is None:
        agg = set([r for r in range(L,R+1)])
    agg &= set([r for r in range(L,R+1)])


print(len(agg))
