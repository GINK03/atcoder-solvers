
N, M = map(int, input().split())
AC = []
for m in range(M):
    a, c = map(int, input().split())
    AC.append( (a, c) )
AC.sort(key=lambda x:x[1])

import math
ans = 0
tmp = N
for a, c in AC:
    gcd = math.gcd(tmp, a)
    ans += (tmp - gcd) * c
    tmp = gcd
print(ans if tmp == 1 else -1)
