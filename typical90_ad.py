

def sieve(n):
    dp = [1]*(n+1) # 初期値ですべてを素数と仮定
    dp[0] = 0; dp[1] = 0
    dp2 = [0]*(n+1)
    for i in range(2, n+1):
        if dp[i]: # もし素数ならば
            dp2[i] += 1
            j = 2 * i # iの倍数はすべて素数ではないはず
            while j <= n:
                dp[j] = 0
                dp2[j] += 1
                j += i 
    # return [i for i in range(n) if dp[i]]
    # print(dp2)
    print(len([x for x in dp2 if x >= K]))


N, K=map(int,input().split())
sieve(N)

