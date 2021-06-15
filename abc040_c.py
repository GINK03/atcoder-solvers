

N = int(input())
*C,=map(int,input().split())
dp = [float("inf")]*(N+10)
dp[0] = 0
for i in range(N):
    if i+2 < N:
        dp[i+2] = min(dp[i+2], dp[i]+abs(C[i+2]-C[i]))
    if i+1 < N:
        dp[i+1] = min(dp[i+1], dp[i]+abs(C[i+1]-C[i]))

print(dp[N-1])
    
