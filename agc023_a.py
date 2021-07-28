
import itertools
import collections

def binomial(n, k):
    if not 0 <= k <= n:
        return 0
    b = 1
    for t in range(min(k, n-k)):
        b *= n
        b //= t+1
        n -= 1
    return b


N = int(input())
*A,=map(int,input().split())
*B,=itertools.accumulate(A)
c = collections.Counter(B)

ans = 0
for num, f in c.items():
    if num == 0 and f < 2:
        ans += 1
    elif num == 0:
        ans += binomial(f+1, 2)
    else:
        ans += binomial(f, 2)
print(ans)
