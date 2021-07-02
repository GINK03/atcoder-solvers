
import collections
N=int(input())
S=input()
b = collections.deque()


c = 0
min_c = 0
for s in S:
    if s == "(":
        c += 1
    else:
        c -= 1
    min_c = min(min_c, c)
tmp = "(" * abs(min_c) + S
print(tmp + ")"*(tmp.count("(") - tmp.count(")")))
