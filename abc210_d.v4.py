import copy
INF = float("INF")
H, W, C = map(int, input().split())
G = [list(map(int, input().split())) for i in range(H)]

def calc_dp(G):
    dp = [[INF] * W for i in range(H)]
    # (i+1, j)はi,jから見たときに、そのままか、そこから移動されるか、駅を設立してから移動するかの安い方を選択
    for i in range(H):
        for j in range(W):
            if i<H-1:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+C, G[i][j]+C)
            if j<W-1:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+C, G[i][j]+C)
    # 最後に駅を設置してそのコストが最小なものを選択
    ans = INF 
    for i in range(H):
        for j in range(W):
            if not (i==0 and j==0):
                ans = min(ans, dp[i][j]+ G[i][j])
    return ans

G0 = copy.deepcopy(G)
G1 = [g[::-1] for g in G]
print(min(calc_dp(G0), calc_dp(G1)))
