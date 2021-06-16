

 
S= str(input())
N = len(S)
T = 'iwi'

if N < 3:
    print(0)
    exit()

dp = [[0]*(N+1) for i in range(N+1)]
#dp[i][j]: 区間[i, j)でTを取り除ける最大値
for i in range(N-2):
    u = S[i:i+3]
    if u == T:
        dp[i][i+3] = 1

for d in range(4, N+1):
    for i in range(N+1-d):
        j = i+d
        # 1. s[i]またはs[j-1]を取り除かない場合
        dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])

        # 2. 区間を分けて取り除く場合
        for k in range(i+1, j):
            dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j])

        # 3. あるkが存在して、[i+1, k), [k+1, j-1)がすべて取り除かれ、
        # s[i]+s[k]+s[j-1]がTと一致する場合
        if S[i] == T[0] and S[j-1] == T[2]:
            for k in range(i+1, j-1):
                if dp[i+1][k]*3 == k-(i+1) and dp[k+1][j-1]*3 == j-1-(k+1) and S[k] == T[1]:
                    dp[i][j] = max(dp[i][j], dp[i+1][k]+dp[k+1][j]+1)

# print("1", dp)
print(dp[0][N])

