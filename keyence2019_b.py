
import re
s=input()

flag = False
if "keyence" in s:
    flag = True
for i in range(1,7):
    h = "keyence"[:i]
    e = "keyence"[i:]

    if re.search(f"^{h}.*?{e}$", s):
        flag = True
    # print(s.find(h), s.find(e))

if flag:
    print("YES")
else:
    print("NO")


