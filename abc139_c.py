import itertools
N=int(input())
H=list(map(int,input().split()))


cnt = 0
tmp = 0
h = list(reversed(H))
for i in itertools.count(0):
    if len(h)-1 == i:
        #cnt += 1
        tmp = max(tmp, cnt)
        break
    if h[i] <= h[i+1]:
        cnt += 1
    else:
        tmp = max(tmp, cnt)
        cnt = 0

print(tmp)
