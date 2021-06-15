

N=int(input())
AS=[]
for _ in range(N):
    *A,=map(int,input().split())
    AS.append(A)

M=int(input())

ban = set()
for m in range(M):
    x,y=map(int,input().split())
    x-=1;y-=1
    ban.add((x,y))
    ban.add((y,x))


import itertools

ans = float('inf')
for ps in itertools.permutations(range(N)):
    ng = False
    tmp = 0
    for i, p in enumerate(ps):
        if i < N-1 and (ps[i], ps[i+1]) in ban:
            ng = True
        tmp += AS[p][i]
    if ng == False:
        ans = min(ans, tmp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
