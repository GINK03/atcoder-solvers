

N,C,K=map(int,input().split())
tmp=[int(input()) for _ in range(N)]
T=[(t, t+K) for t in tmp]
T.sort(key=lambda x:x[1])

cnt = 0
while T:
    print(T)
    head_t, head_end = T.pop(0)
    for i in range(0, C-1):
        if not T:
            break
        if T[0][0] <= head_end:
            T.pop(0)
    
    cnt += 1
print(cnt)

    
