
N, K = map(int, input().split())

A, B = [], []
for n in range(N):
    a,b = map(int, input().split())
    A.append(a); B.append(b)

H = max(A + [K]) + 1
W = max(B + [K]) + 1
G = [[0]*(W+1) for _ in range(H+1)]
for h, w in zip(A, B):
    G[h+1][w+1] += 1

for h in range(1, H+1):
    for w in range(1, W+1):
        G[h][w] += G[h-1][w] 
for h in range(1, H+1):
    for w in range(1, W+1):
        G[h][w] += G[h][w-1] 

ans = 0
for h in range(H-K):
    for w in range(W-K):
        tmp = G[h][w] + G[h+K+1][w+K+1] - G[h][w+K+1] - G[h+K+1][w]
        ans = max(ans, tmp)
print(ans)
