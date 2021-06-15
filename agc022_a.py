
from collections import Counter
from string import ascii_lowercase
 
S = input()
 
cnt = Counter(S)
can = set(ascii_lowercase) ^ set(S)
if len(S) < 26:
    S += " "
 
ans = -1
lst_S = list(S)
while lst_S:
    s_end = lst_S.pop()
    ok = list(filter(lambda s: s_end < s, can))
    if ok:
        ans = "".join(lst_S) + str(min(ok))
        break
    can.add(s_end)
 
print(ans)

