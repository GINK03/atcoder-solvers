
import itertools

N = int(input())
S = input()

res = []
for k, gi in itertools.groupby(S, key=lambda x:x[0]):
    res.append(k)
    res.append(len(list(gi)))
# print(res)

res = 0
for k, gi in itertools.groupby(S, key=lambda x:x[0]):
    l = len(list(gi))
    res += l * (l+1) // 2
print(N * (N + 1) // 2 - res)

