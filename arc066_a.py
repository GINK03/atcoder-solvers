
import collections
N = int(input())
*A,=map(int,input().split())
MOD = 10**9 + 7

if N%2 == 0:
    if all([v==2 for v in collections.Counter(A).values()]):
        print(2**(N//2)%MOD)
    else:
        print(0)
else:
    if A.count(0) == 1:
        A.remove(0)
        if all([v==2 for v in collections.Counter(A).values()]):
            print(2**(N//2)%MOD)
        else:
            print(0)
    else:
        print(0)
