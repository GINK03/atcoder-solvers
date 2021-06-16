

H,N=map(int,input().split())


dp = [float("inf")]*(2*(10**4))
dp[0] = 0

AB = []
for _ in range(N):
    a,b =map(int,input().split())
    AB.append( (a,b) )

for a, b in AB:
    for i in range(len(dp)):
        if i >= a:
            dp[i] = min(dp[i-a]+b, dp[i])

print(min(dp[H:]))
