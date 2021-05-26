N=int(input())
ax=list(map(int,input().split()))
import collections

b = collections.defaultdict(int)
overs = 0
for a in ax:
    if 1 <= a <= 399:
        b[1] +=1
    if 400 <= a <= 799:
        b[2] +=1
    if 800 <= a <= 1199:
        b[3] +=1
    if 1200 <= a <= 1599:
        b[4] +=1
    if 1600 <= a <= 1999:
        b[5] +=1
    if 2000 <= a <= 2399:
        b[6] +=1
    if 2400 <= a <= 2799:
        b[7] +=1
    if 2800 <= a <= 3199:
        b[8] +=1
    if 3200 <= a:
        overs+=1


min_count = sum([1 for k,v in b.items() if v != 0])

if min_count == 0:
    print(1, overs)
else:
    print(min_count, min_count+overs)

