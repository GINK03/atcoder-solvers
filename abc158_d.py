

import collections

s=list(input())
que = collections.deque(s)
Q=int(input())

rev = 0
for _ in range(Q):
    raw = input()
    if raw[0] == "1":
        rev += 1
    else:
        _, o, char = raw.split()
        if o == "1":
            if rev%2 == 0:
                que.appendleft(char)
            else:
                que.append(char)
        else:
            if rev%2 == 0:
                que.append(char)
            else:
                que.appendleft(char)
if rev%2 == 0:
    print(*que, sep="")
else:
    print(*list(que)[::-1], sep="")
