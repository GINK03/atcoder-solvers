H,W=map(int,input().split())
h,w=map(int,input().split())

buff = []
for w1 in range(W):
    buff.append([0 for h1 in range(H)])

for w2 in range(w):
    for x in range(H):
        buff[w2][x] = 1
    for h2 in range(h):
        for x in range(W):
            buff[x][h2] = 1
c = 0
for b in buff:
    for a in b:
        if a == 0:
            c+=1
print(c)
