

H,W=map(int,input().split())


cnt = 0
ss = ""
for h in range(H):
    s = ""
    for w in range(W):
        if w%2 == 0 and  h%2 == 0:
            s += "#"
            cnt += 1
        else:
            s += "."
    ss += s + '\n'

if H == 1 or W == 1:
    print(H*W)
else:
    print(cnt)

