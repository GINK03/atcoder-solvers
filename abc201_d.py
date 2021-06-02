
H,W=map(int,input().split())
A=[list(input()) for _ in range(H)]

dp = [[0]*(W+2) for _ in range(H+2)]



def check(h,w):
    if h >= H or w >= W:
        return -10**18
    if A[h][w] == "+":
        return 1
    else:
        return -1

# 後ろから(結果から)見ていくdp
for h in range(H-1, -1, -1):
    for w in range(W-1,-1, -1):
        if h == H-1 and w == W-1:
            continue
        if (h+w)%2 == 0:
            # 高橋さんの操作で昔から今(点数が大きい方から来ているはずである)
            dp[h][w] = max( dp[h+1][w] + check(h+1,w), dp[h][w+1] + check(h,w+1) )
        else:
            # 青木さんの操作で昔から今(点数が小さい方から来ているはずである)
            dp[h][w] = min( dp[h+1][w] - check(h+1,w), dp[h][w+1] - check(h,w+1) )

if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] == 0:
    print("Draw")
else:
    print("Aoki")
