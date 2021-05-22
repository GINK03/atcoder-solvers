

N,M=map(int,input().split())
A=list(map(int,input().split()))

dp=[float('inf')]*(N+10)
dp[0] = 0
for a in A:
    for j in range(len(dp)):
        if j >= a:
            dp[j] = min(dp[j], dp[j-a] + 1)
#print(dp)
print(dp[N])
