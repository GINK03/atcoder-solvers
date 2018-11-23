n = input()
from collections import Counter
xs = list(input())
o = dict(Counter(xs))
for c in '1234':
  o[c] = 0 if c not in o else o[c]
a = sorted([v for k,v in o.items()], key=lambda x:x)
m,M = a[0], a[-1]
print(M,m)

