import heapq

N,K=map(int,input().split())

A, B = [], []
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append((-b, a-b))

heapq.heapify(B)

cnt = 0
acc = 0
while B:
    nb, a = heapq.heappop(B)
    acc += -nb
    heapq.heappush(B, (-a, 0)) 
    cnt += 1
    if cnt == K:
        break
print(acc)

