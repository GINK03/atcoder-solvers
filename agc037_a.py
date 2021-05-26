import itertools
import collections
S=input()

que = collections.deque(list(S))

cnt = 0
char = ''
while que:
    if que[0] == char:
        if len(que) <= 1:
            break
        else:
            char = que.popleft() + que.popleft()
            cnt += 1
    else:
        cnt += 1
        char = que.popleft()
print(cnt)




