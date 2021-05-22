H,W=map(int,input().split())

C=[ [float('inf')]*10 for _ in range(10)]

for i in range(10):
    for j, ch in enumerate(input().split()):
        C[i][j] = int(ch)


# ワーシャルフロイド法
for k in range(0, 10):
    for x in range(0, 10):
        for y in range(0, 10):
            C[x][y] = min(C[x][y], C[x][k] + C[k][y])

ans = 0
for h in range(H):
    strs = input().split()
    for s in strs:
        s = int(s)
        if s == -1:
            continue
        ans += C[s][1]
print(ans)

