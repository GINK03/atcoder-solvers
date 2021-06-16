
N,K=map(int,input().split())

que = []
for _ in range(N):
    a,b = map(int,input().split())
    que.append( (a,b) )

import heapq

heapq.heapify(que)

cnt = 0
acc = 0
while que:
    a, b = heapq.heappop(que)
    cnt += 1
    acc += a
    heapq.heappush(que, (a + b, b))

    if cnt >= K:
        break

#print(cnt)
print(acc)
    
