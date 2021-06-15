
import collections
S=input()
que = collections.deque(S)
prv = que.popleft()
cnt = 1
buff = ""
while que:
    a = que.popleft()
    if prv == a:
        cnt += 1
        prv = a
        continue
    buff += prv + str(cnt)
    prv = a
    cnt = 1
buff += prv + str(cnt)

print(buff)
