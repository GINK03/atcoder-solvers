H,W=map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

ha = [sum([A[h][w] for w in range(W)]) for h in range(H)]
wa = [sum([A[h][w] for h in range(H)]) for w in range(W)]



B = A.copy()
for h in range(H):
    for w in range(W):
        B[h][w] = ha[h] + wa[w] - A[h][w] 

[print(*b, sep=" ") for b in B]
