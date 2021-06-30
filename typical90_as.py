

def main():
    N,K=map(int,input().split())
    X,Y = [], []
    for _ in range(N):
        x,y=map(int,input().split())
        X.append(x); Y.append(y)

    # すべての点の距離を計算
    d = dict()
    for i in range(N):
        for j in range(N):
            d[(i,j)] = (X[i]-X[j])**2 + (Y[i]-Y[j])**2

    # すべてのビットパターンの重みを記録
    cost = [0]*(1<<N)
    for i in range(1<<N):
        for j in range(N):
            for k in range(j):
                if i&(1<<j) > 0 and i&(1<<k) > 0:
                    cost[i] = max(cost[i], d[(j,k)])


    dp = [[float("inf")]*(1<<N) for _ in range(K+1)]
    dp[0][0] = 0
    for i in range(1,K+1):
        for j in range(1, 1<<N):
            k = j
            # jで立っているすべてのbitについてフラグを折ったらどうなるかを見ていく
            while k != 0:
                dp[i][j] = min(dp[i][j], max(dp[i - 1][j - k], cost[k]))
                k = (k - 1) & j

    print( dp[K][(1 << N) - 1])

if __name__ == "__main__":
    main()
