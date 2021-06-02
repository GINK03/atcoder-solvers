 
N,M=map(int,input().split())


cnt = 0
if N*2 < M:
    cnt += N
    M -= N*2
    cnt += M//4
    print(cnt)
else:
    cnt += M//2
    print(cnt)

