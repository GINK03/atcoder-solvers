N,M,Q=map(int,input().split())

"""
# このアプローチはメモリーエラー
s=[[1]]

#長さNまで
import copy
while True:
    n = []
    for s1 in s:
        for append in range(s1[-1], M+1):
            n1 = copy.copy(s1)
            n1.append(append)
            n.append(n1)
    if len(n[0]) > M:
        break
    s = n
#for s1 in s:
#    print(s1)
iidp = [list(map(int,input().split())) for q in range(Q)]

al = 0
for s1 in s:
    a = 0
    for i1, i2, d, p in iidp:
        if s1[i2-1] - s1[i1-1] == d:
            a += p
    al = max(a,al)

print(al)
"""

iidp = [list(map(int,input().split())) for q in range(Q)]
import itertools
al = 0
for s1 in itertools.combinations_with_replacement(list(range(1,M+1)), N):
    a = 0
    for i1, i2, d, p in iidp:
        if s1[i2-1] - s1[i1-1] == d:
            a += p
    al = max(a,al)

print(al)
