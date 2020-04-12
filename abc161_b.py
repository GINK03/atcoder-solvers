n,m=map(int,input().split())
ax = list(map(int,input().split()))
allnum = sum(ax)
ax=[a for a in ax if a >= allnum/(4*m)]

if len(ax) >= m:
    print("Yes")
else:
    print("No")
