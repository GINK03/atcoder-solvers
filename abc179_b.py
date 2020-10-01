import re
n=int(input())

s = ""
for _ in range(n):
    d1,d2 = input().split()
    if d1==d2:
        s+="1"
    else:
        s+="0"
#print(s)
try:
    a = max([len(x) for x in re.findall(r"1+", s)])
    if a >= 3:
        print("Yes")
    else:
        print("No")
except:
    print("No")
