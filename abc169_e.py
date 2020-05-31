import math
import statistics

ms = set()
for i in range(2,3+1):
    for j in range(3,5+1):
        for k in range(4, 6+1):
            a = sorted([i,j,k])
            m = statistics.median(a) 
            ms.add(m)
print(ms)
print(len(ms))

"""
ms = set()
for i in range(1,2+1):
    for j in range(2,5+1):
        a = sorted([i,j])
        m = statistics.median(a) 
        ms.add(m)
print(ms)
print(len(ms))
"""

n=int(input())
ab = []
for _ in range(n):
    a,b=map(int,input().split())
    ab.append((a,b))


pool = []
for a,b in ab:
    af = sum([1 for a1,b1 in list(ab) if a1 <= a <= b1])
    bf = sum([1 for a1,b1 in list(ab) if a1 <= b <= b1])
    pool.append((a,af))
    pool.append((b, bf))

# print(pool)

max_pool = max([p[1] for p in pool])

if n%2 == 0:
    # print(pool)
    #pool = [p[0] for p in pool if p[1] >= max_pool-1]
    #print(max(pool) - min(pool) + 1)
    if max_pool%2 == 0:
        pool = [p[0] for p in pool if p[1] >= max_pool-1]
        print(max(pool) - min(pool) + 1)
    else:
        pool = [p[0] for p in pool if p[1] >= max_pool]
        print(max(pool) - min(pool) + 1)
else:
    # print(pool)
    if max_pool%2 == 0:
        pool = [p[0] for p in pool if p[1] >= max_pool]
        print(max(pool) - min(pool) + 1)
    else:
        pool = [p[0] for p in pool if p[1] >= max_pool-1]
        print(max(pool) - min(pool) + 1)

