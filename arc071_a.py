import collections
N=int(input())

lst =[]
for _ in range(N):
    s = input()
    tmp = collections.Counter(s)
    lst.append(tmp)

a = set(lst[0].keys())
for b in lst:
    a &= set(b.keys())

base = {x:float('inf') for x in a}
for tmp in lst:
    for x in a:
        base[x] = min(base[x], tmp[x])
# print(base)

print("".join([x*i for x,i in sorted(base.items())]))

