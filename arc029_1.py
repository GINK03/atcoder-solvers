N=int(input())
A=[]
for _ in range(N):
    A.append(int(input()))

P=1<<N

ans = float('inf')
for i in range(P):
    l,r=0,0
    for j in range(N):
        if i&(1<<j) > 0:
            l += A[j]
        else:
            r += A[j]
    ans=min(ans, max(l,r))

print(ans)

