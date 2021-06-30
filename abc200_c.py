import collections
import math
N=int(input())
*A,=map(int,input().split())
R=[a%200 for a in A]
dic = collections.Counter(R)

ans = 0
for k,f in dic.items():
    if f == 1:
        continue
    ans += math.comb(f, 2)
print(ans)
