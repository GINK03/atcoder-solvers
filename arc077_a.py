import collections

N=int(input())
A=list(map(int,input().split()))

que = collections.deque([])

for i, a in enumerate(A):
    if i%2:
        que.appendleft(a)
    else:
        que.append(a)
if N%2 == 0:
    print(" ".join(map(str, que)))
else:
    a = list(map(str, que))[::-1]
    print(" ".join(a))

