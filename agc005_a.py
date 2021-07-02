import collections
X = list(input())
que = collections.deque([])

for x in X:
    if x == "S":
        que.append(x)
    else:
        if len(que) > 0:
            if que[-1] == "S":
                que.pop()
            else:
                que.append(x)
        else:
            que.append(x)

print(len(que))
