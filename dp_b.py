

N,K = map(int, input().split())
*C,=map(int,input().split())
dp = [float("inf")]*(N+10)
dp[0] = 0
for i in range(N):
    for k in range(K+1):
        if i+k < N:
            dp[i+k] = min(dp[i+k], dp[i]+abs(C[i+k]-C[i]))

print(dp[N-1])
    
