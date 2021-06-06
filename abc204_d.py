import collections
N=int(input())
*T,=map(int,input().split())
T.sort()

sum_t = sum(T)




tgt = sum_t/2
# print(sum_t, tgt)

dp = [[0]*(sum_t+10) for _ in range(N+1)]
dp[0][0] = 1
for i, t in enumerate(T):
    for j in range(0, sum_t+10):
        if j >= t:
            dp[i+1][j] = max(dp[i][j], dp[i][j-t])
            # dp[i+1][j] = dp[i][j-t] 
        else:
            dp[i+1][j] = dp[i][j]
            ...
# print([i for i,v in enumerate(dp[-1]) if v > 0])
C = [i for i,v in enumerate(dp[-1]) if v > 0]
al = [(abs(c-tgt),c) for c in C]
al.sort()

# print(al)

delta, v0 = al[0]
v1 = sum_t - v0

print(max(v0, v1))
