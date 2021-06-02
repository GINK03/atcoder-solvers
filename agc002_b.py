
N,M=map(int,input().split())

dp = [False]*N
dp[0] = True
dpq = [1]*N

for m in range(M):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    dpq[x] -= 1
    dpq[y] += 1
    if dp[x]:
        dp[y] = True
    if dpq[x] == 0:
        dp[x] = False

print(sum(dp))
