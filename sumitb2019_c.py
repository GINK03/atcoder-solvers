import itertools

X = int(input())
ps = [100, 101, 102, 103, 104, 105]
dp=[0]*(X+1)
dp[0] = 1

for p in ps:
    for i in range(len(dp)):
        if i >= p:
            dp[i] = max(dp[i], dp[i-p])

print(dp[X])
