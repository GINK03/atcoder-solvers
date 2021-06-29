import collections

Q = int(input())

que = collections.deque([])
for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        que.appendleft(x)
    if t == 2:
        que.append(x)
    if t == 3:
        print(que[x-1])
