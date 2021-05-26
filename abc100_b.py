

import itertools
ans = [[] for _ in range(3)] 
for a in [0,1,2]:
    o = 100**a
    n = 100**(a+1)
    for i in itertools.count(1):
        if i%o==0 and i%n !=0:
            ans[a].append(i)
        if len(ans[a]) == 100:
            break

D,N=map(int,input().split())

print(ans[D][N-1])
