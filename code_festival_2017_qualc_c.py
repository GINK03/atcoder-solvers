import collections

s = input()
que = collections.deque(s)

cnt = 0
while que:
    h, t = que[0], que[-1]
    if h == "x" and t != "x":
        que.append("x")
        cnt += 1
    elif h != "x" and t == "x":
        que.appendleft("x")
        cnt += 1
    elif len(que) == 1:
        break
    elif h == t:
        que.pop()
        que.popleft()
    else:
        print(-1); exit()

print(cnt)
