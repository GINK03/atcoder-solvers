
import collections
S=input()
que = collections.deque(S)

while que:
    lc = que.pop()
    if lc in {"o", "k", "u"}:
        continue
    elif lc == "h" and len(que) > 0 and que[-1] == "c":
        que.pop()
        continue
    else:
        print("NO")
        exit()
print("YES")
