
N,K=map(int,input().split())


A = [list(map(int,input().split())) for _ in range(N)]
A.sort()
cnt = 0
for a, b in A:
    cnt += b
    if cnt >= K:
        print(a)
        break
