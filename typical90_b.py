
import collections

N = int(input())

def check(s):
    st = 0
    for i in range(len(s)):
        if s[i] == "(":
            st += 1
        else:
            st -= 1
        if st < 0:
            return False
    if st == 0:
        return True
    else:
        return False

buff = []
for i in range(1<<N):
    s = ""
    for j in range(N):
        if i & (1<<j) > 0:
            s += "("
        else:
            s += ")"
    if check(s):
        buff.append(s)
buff.sort()
print(*buff, sep='\n')




