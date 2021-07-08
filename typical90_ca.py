
H,W=map(int,input().split())

A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]


cnt = 0
for h in range(H):
    for w in range(W):
        if A[h][w] != B[h][w]:
            d = B[h][w] - A[h][w]
            cnt += abs(d)
            for dh, dw in [(0,0), (1,0), (0, 1), (1,1)]:
                nh,nw = h+dh, w+dw
                if not(0<=nh<H and 0<=nw<W):
                    print("No")
                    exit()
                B[nh][nw] -= d

if A == B:
    print("Yes")
    print(cnt)
else:
    print("No")
