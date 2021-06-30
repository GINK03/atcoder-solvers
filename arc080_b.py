

H,W = map(int,input().split())
N = int(input())
*A,=map(int,input().split())


G = [[0]*W for _ in range(H)]
cur = 0
for i in range(N):
    a_num = A[i]
    clr = i+1

    for _ in range(a_num):
        nh = cur // W
        nw = cur % W

        if nh%2 == 0:
            G[nh][nw] = clr
        else:
            G[nh][W-nw-1] =  clr
        
        cur += 1


[print(*g, sep=" ") for g in G]

