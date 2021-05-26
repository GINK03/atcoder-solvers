
N=int(input())
A=list(map(int,input().split()))
A.sort()
import itertools
pows= []
for cnt in itertools.count(1):
    if (1<<cnt) > 10**9:
        break
    pows.append( (1<<cnt,cnt) )
pows = list(reversed(pows))

acc = 0
for a in A:
    for pow, cnt in pows:
        if a%pow == 0:
            #print(a, pow, cnt, acc)
            acc += cnt
            break
print(acc)

