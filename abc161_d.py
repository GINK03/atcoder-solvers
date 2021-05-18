import collections

K=int(input())


que = collections.deque([i for i, cnt in zip(range(1,10), range(1,10))])

cnt = 1
while que:
    i = que.popleft()
    if cnt == K:
        print(i)
        break
    cnt += 1
    if i%10 != 0:
        ni = 10*i+i%10-1
        que.append(ni)
    que.append(10*i + i%10)
    if i%10 != 9:
        que.append(10*i+i%10+1)



