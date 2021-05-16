S=input()
SI = list(map(int, S))

size=len(S)
P = 1<<(size-1)


total = 0
for i in range(P):
    bm = []
    for j in range(size):
        bm.append(int(i&(1<<j) > 0))
    acc = []
    s = bm[0]
    buf = SI[0]
    for i in range(1, size):
        if bm[i] == s:
            buf = 10*buf + SI[i]
        else:
            acc.append(buf)
            s = bm[i]
            buf = SI[i]
    acc.append(buf)
    total += sum(acc)

print(total)
            
