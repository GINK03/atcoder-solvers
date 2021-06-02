import collections

K=int(input())


inits = list(range(1,10))

# bfs

que = collections.deque(inits)

cnt = 0
while que:
    i = que.popleft()
    cnt += 1
    if cnt == K:
        print(i)
        break
    # 1引く
    if i%10 != 0:
        que.append(i*10 + i%10 - 1)
    # 同じ数で増える
    que.append(i*10 + i%10)
    # 一個足す
    if i%10 != 9:
        que.append(i*10 + i%10 + 1)



