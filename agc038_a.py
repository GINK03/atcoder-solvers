

H,W,A,B = map(int,input().split())

G = [[0]*W for h in range(H)]

for h in range(B):
    for w in range(A, W):
        G[h][w] = 1

for h in range(B,H):
    for w in range(A):
        G[h][w] = 1


for g in G:
    print(*g, sep="")

