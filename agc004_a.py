

import itertools
A=list(map(int,input().split()))
ans = float('inf')
for i0,i1,i2 in itertools.permutations([0,1,2]):
    a=A[i0]//2
    b,c=A[i1],A[i2]
    ans = min(b*c*(A[i0]-a-a), ans)
print(ans)

