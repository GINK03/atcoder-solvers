
H, W = map(int, input().split())
G = [list(map(int, input().split())) for h in range(H)]

ans = []
for h in range(H):
    for w in range(W-1):
        if G[h][w]%2 == 1:
            G[h][w+1] += 1
            G[h][w] -= 1
            ans.append( (h, w, h, w+1) )
for h in range(H-1):
    for w in range(W):
        if G[h][w]%2 == 1:
            G[h+1][w] += 1
            G[h][w] -= 1
            ans.append( (h, w, h+1, w) )

print(len(ans))
for rec in ans:
    print(*[r+1 for r in rec])


