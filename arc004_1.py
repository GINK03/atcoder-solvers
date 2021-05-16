N=int(input())

dp=[[0]*N for _ in range(N)]

A=[]
for _ in range(N):
    x,y=map(int,input().split())
    A.append((x,y))

for i in range(N):
    for j in range(N):
        dp[i][j] = ((A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2)**0.5

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(dp[i][j], ans)

print(ans)
