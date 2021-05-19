import collections
N = int(input())
S = list(map(int, input()))


si = collections.defaultdict(list)
for i, s in enumerate(S, 0):
    si[s].append(i)
for s in si.keys():
    si[s].sort()

import bisect
cnt = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if not si[i] or not si[j] or not si[k]:
                continue
            i1 = si[i][0]
            t2 = bisect.bisect_right(si[j], i1)
            if t2 >= len(si[j]):
                continue
            i2 = si[j][t2] 
            t3 = bisect.bisect_right(si[k], i2)
            if t3 >= len(si[k]):
                continue
            i3 = si[k][t3] 
            #if (2,2,4) == (i,j,k):
            #    print( (i,j,k),  si[i], si[j], si[k], (i1,i2,i3) )
            cnt += 1

print(cnt)
