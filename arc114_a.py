
import itertools
import functools
import math

N=int(input())
*X,=map(int,input().split())

def sieve(n):
    dp = [1]*(n+1) # 初期値ですべてを素数と仮定
    dp[0] = 0; dp[1] = 0
    for i in range(2, n+1):
        if dp[i]: # もし素数ならば
            j = 2 * i # iの倍数はすべて素数ではないはず
            while j <= n:
                dp[j] = 0
                j += i 
    return [i for i in range(n) if dp[i]] 


def ng():
    cans = set()
    for x in X:
        for p in ps:
            if x%p == 0:
                cans.add(p) # 最小の素数が答えの候補に常になるわけではない罠
                break
    import functools
    print(functools.reduce(lambda x,y:x*y,cans))

def ans_of_editor():
    ps = sieve(50)
    P=[(p,0) for p in ps]
    ans = float('inf')
    for ops in itertools.product(*P):
        *ps, = filter(lambda x:x, ops)
        if ps == []:
            continue
        elif len(ps) == 1:
            y = ps[0]
        else:
            y = functools.reduce(lambda x,y:x*y,ps)    

        if all([math.gcd(x,y) > 1 for x in X]):
            ans = min(ans, y)
    print(ans)

ans_of_editor()
