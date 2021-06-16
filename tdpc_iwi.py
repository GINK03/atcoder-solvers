

 
s = str(input())
n = len(s)
t = 'iwi'

if n < 3:
    print(0)
    exit()

dp = [[0]*(n+1) for i in range(n+1)]
#dp[i][j]: 区間[i, j)でTを取り除ける最大値
for i in range(n-2):
    u = s[i:i+3]
    if u == t:
        dp[i][i+3] = 1

for d in range(4, n+1):
    for i in range(n+1-d):
        j = i+d
        # s[i]またはs[j-1]を取り除かない場合
        dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])
        # 区間を分けて取り除く場合
        for k in range(i+1, j):
            dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j])
        # あるkが存在して、[i+1, k), [k+1, j-1)がすべて取り除かれ、
        # s[i]+s[k]+s[j-1]がtと一致する場合
        if s[i] == t[0] and s[j-1] == t[2]:
            for k in range(i+1, j-1):
                if dp[i+1][k]*3 == k-(i+1) and dp[k+1][j-1]*3 == j-1-(k+1) and s[k] == t[1]:
                    dp[i][j] = max(dp[i][j], dp[i+1][k]+dp[k+1][j]+1)
# print(dp)
print(dp[0][n])
 
