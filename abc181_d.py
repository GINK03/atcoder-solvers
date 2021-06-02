
import numpy as np
import collections
import itertools

# 8の倍数は下三桁が8の倍数であること
ops = set()
for i in range(100, 10**4):
    if i%8 == 0:
        ops.add("".join(sorted(str(i)[-3:])))
# 108通りしかない
ops = [dict(collections.Counter(op)) for op in ops]

S = input()

if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

S = dict(collections.Counter(S))

checks = []
for op in ops:
    checks.append( all([S.get(k,0)-v>=0 for k, v in op.items()]) )
if any(checks):
    print("Yes")
else:
    print("No")

