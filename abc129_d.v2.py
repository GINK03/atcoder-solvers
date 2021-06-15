H, W = map(int, input().split())

G = [list(input()) for _ in range(H)]

D = dict()
for tp in ["u", "d", "l", "r"]:
    D[tp] = [[0] * W for i in range(H)]

for i in reversed(range(H)):
    for j in range(W):
        if G[i][j] == '.' and i < H - 1:
            D["u"][i][j] = D["u"][i + 1][j] + 1
        elif G[i][j] == '.':
            D["u"][i][j] = 1
for i in range(H):
    for j in range(W):
        if G[i][j] == '.' and i > 0:
            D["d"][i][j] = D["d"][i - 1][j] + 1
        elif G[i][j] == '.':
            D["d"][i][j] = 1
for i in range(H):
    for j in reversed(range(W)):
        if G[i][j] == '.' and j < W - 1:
            D["l"][i][j] = D["l"][i][j + 1] + 1
        elif G[i][j] == '.':
            D["l"][i][j] = 1
for i in range(H):
    for j in range(W):
        if G[i][j] == '.' and j > 0:
            D["r"][i][j] = D["r"][i][j - 1] + 1
        elif G[i][j] == '.':
            D["r"][i][j] = 1
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, D["u"][i][j] + D["d"][i][j] + D["l"][i][j] + D["r"][i][j] - 3)
print(ans)
