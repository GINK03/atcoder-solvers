
N=int(input())

dp = [float("inf")] * (N+100)
dp[0] = 0

for i in range(N):
    if i+1 < len(dp):
        dp[i+1] = min(dp[i+1], dp[i]+1)
   
    r = 6
    while True:
        if i+r < len(dp):
            dp[i+r] = min(dp[i+r], dp[i]+1)
        else:
            break
        r *= 6

    r = 9
    while True:
        if i+r < len(dp):
            dp[i+r] = min(dp[i+r], dp[i]+1)
        else:
            break
        r *= 9
# print(dp)
print(dp[N])
