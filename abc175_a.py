
import re
s=input()

rs = [len(x) for x in re.findall("R{1,}", s)]

if rs == []:
    print(0)
else:
    print(max(rs))
