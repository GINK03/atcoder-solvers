import sys; sys.setrecursionlimit(10**9)

def wrap():
    N = int(input())
    if N == 0:
        exit(0)
    *W,=map(int,input().split())
    dp = [[-1]*(N+2) for _ in range(N+2)]
    def rec(l = 0, r = N): # メモ化再帰
        if (r - l) <= 1:
            return 0
        if (r - l) == 2:
            if abs(W[l] - W[l + 1]) <= 1: # 隣り合う2つの差が1以下
                return 2
            else:
                return 0
        if dp[l][r] != -1:
            return dp[l][r] # 既に計算済みならその値を使う
        # 1. 全部取り除けるとき
        if abs(W[l] - W[r-1]) <= 1 and rec(l + 1, r - 1) == r - l - 2:
            dp[l][r] = max(dp[l][r], r - l)
        # 2. そうでない時
        for i in range(l+1, r-1+1):
            dp[l][r] = max(dp[l][r], rec(l, i) + rec(i, r))
        return dp[l][r]
    print(rec())

while True:
    wrap()
