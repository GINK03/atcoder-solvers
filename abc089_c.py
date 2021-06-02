import itertools
N=int(input())
S = [input() for _ in range(N)]
S.sort()

tmp = [(k,len(list(v))) for k,v in itertools.groupby(S, key=lambda x:x[0]) if k in "MARCH"]

acc = 0
for e0, e1, e2 in itertools.combinations(tmp, 3):
    acc += (e0[1] * e1[1] * e2[1])
print(acc)

