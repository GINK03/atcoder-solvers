N=int(input())
A=list(map(int,input().split()))

POINTS_MAX = 100*100 + 10
dp = [[0]*POINTS_MAX for _ in range(len(A)+1)]
dp[0][0] = 1
for i in range(len(A)):
    for j in range(POINTS_MAX):
        dp[i+1][j] |= dp[i][j] # 上の状態と同じ
        if j >= A[i]: # itemを選択できるならば
            dp[i+1][j] |= dp[i][j-A[i]] # 前のアイテムが有るならばtrueになる(アイテムがtrueをフォワードできる)

print(sum(dp[len(A)]))
