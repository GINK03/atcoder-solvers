
import collections
N,C,K=map(int,input().split())
tmp=[int(input()) for _ in range(N)]
T=[(t, t+K) for t in tmp]
T.sort(key=lambda x:x[1])

que = collections.deque(T)

cnt = 0
while que:
    # print(que)
    head_t, head_end = que.popleft()
    for i in range(0, C-1):
        if not que:
            break
        if que[0][0] <= head_end:
            que.popleft()
        else:
            break
    
    cnt += 1
print(cnt)

    
