A,B,M=map(int,input().split())
ax=list(map(int,input().split()))
bx=list(map(int,input().split()))

ans = min(ax) + min(bx)

for _ in range(M):
    x,y,c=map(int,input().split())
    x-=1;y-=1;
    ans = min(ans, ax[x]+bx[y]-c)
print(ans)

