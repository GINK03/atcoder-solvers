
INF = float("INF")
def solve(H, W, C, A):
    dp = []
    X = []
    for i in range(H + 1):
        dpl = []
        Xl = []
        for j in range(W + 1):
            dpl.append(INF)
            Xl.append(INF)
        dp.append(dpl)
        X.append(Xl)
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = min(A[i - 1][j - 1], dp[i - 1][j] + C, dp[i][j - 1] + C)
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            X[i][j] = min(dp[i - 1][j] + C + A[i - 1][j - 1], dp[i][j - 1] + C + A[i - 1][j - 1])
    return X
 
def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans1 = solve(H, W, C, A)
    B = []
    for i in range(H):
        B.append(A[i][::-1])
    ans2 = solve(H, W, C, B)
 
    minval = 10 ** 64
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            minval = min(minval, ans1[i][j], ans2[i][j])
    return minval
 
if __name__ == '__main__':
    print(main())
