
H,W,K=map(int,input().split())

G = [list(input()) for h in range(H)]

cnt = 1
for h in range(H):
    for w in range(W):
        if G[h][w] == "#":
            G[h][w] = cnt
            cnt += 1
        else:
            G[h][w] = 0



for h in range(H):
    for w in range(W-1):
        if G[h][w] != 0 and G[h][w+1] == 0:
            G[h][w+1] = G[h][w]

for h in range(H):
    for w in range(1,W)[::-1]:
        if G[h][w] != 0 and G[h][w-1] == 0:
            G[h][w-1] = G[h][w]

for h in range(H-1):
    for w in range(W):
        if G[h][w] != 0 and G[h+1][w] == 0:
            G[h+1][w] = G[h][w]

for h in range(1, H)[::-1]:
    for w in range(W):
        if G[h][w] != 0 and G[h-1][w] == 0:
            G[h-1][w] = G[h][w]

#import numpy as np
#print(np.array(G))
for g in G:
    print(*g, sep=" ")
