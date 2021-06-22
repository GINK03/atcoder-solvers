
N = int(input())
*A,=map(int,input().split())

import collections
import math
dic = collections.Counter(A)
#print(dic)
ans = 1
for k,v in dic.items():
    #print( N-v, v)
    ans += (N-v)*v
#print(ans)
print(ans//2)
    
