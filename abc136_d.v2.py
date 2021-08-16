import itertools
S = input()

l = []
for k, gi in itertools.groupby(S):
    l.append( (k, len(list(gi))) )
ans = [0] * len(S)
pos = 0
for k, ln in l:
    if k == "R":
        for i in range(ln):
            if i%2 == 0:
                ans[pos+ln-1] += 1
            else:
                ans[pos+ln] += 1
    if k == "L":
        for i in range(ln):
            if i%2 == 0:
                ans[pos] += 1
            else:
                ans[pos-1] += 1
    pos += ln
print(*ans, sep=" ")


