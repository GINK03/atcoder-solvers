import collections
N=int(input())
S=[input() for i in range(N)]
S=collections.Counter(S)
max_v = max(S.values())
for k,v in sorted(list(filter(lambda x:x[1]==max_v, S.items()))):
    print(k)

