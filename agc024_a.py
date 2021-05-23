
*X,K=map(int,input().split())

cycle = []
for k in range(1,3):
    t0=X[1]+X[2]
    t1=X[0]+X[2]
    t2=X[0]+X[1]
    X=[t0, t1, t2]
    ans = t1-t0
    cycle.append(ans)

if K%2==0:
    print(cycle[0])
else:
    print(cycle[1])
