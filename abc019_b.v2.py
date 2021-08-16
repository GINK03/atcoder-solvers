import itertools

S=input()

tmp = []
for k,gi in itertools.groupby(S):
    tmp.append(k)
    tmp.append(str(len(list(gi))))
print("".join(tmp))

