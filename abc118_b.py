
N,M=map(int,input().split())
dp=[0]*M
for i in range(N):
    k,*ans=map(int,input().split())
    for a in ans:
        dp[a-1]+=1
print(dp.count(N))
# print(dp)
