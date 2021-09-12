import copy
inf = float("inf")
H, W, C = map(int, input().split())

G = [list(map(int, input().split())) for h in range(H)]

def calc(G):
    dp = [[inf]*(W+1) for h in range(H+1)]
    for h in range(H):
        for w in range(W):
            dp[h+1][w] = min(dp[h+1][w], dp[h][w] + C, G[h][w] + C)
            dp[h][w+1] = min(dp[h][w+1], dp[h][w] + C, G[h][w] + C)
    ans = inf
    for h in range(H):
        for w in range(W):
            if h == w == 0:
                continue
            ans = min(ans, dp[h][w] + G[h][w])
    return ans

G0 = copy.deepcopy(G)
G1 = [g[::-1] for g in G]
print(min(calc(G0), calc(G1)))
