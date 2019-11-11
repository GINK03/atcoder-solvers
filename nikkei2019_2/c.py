N = int(input())
ax = list(map(int,input().split()))
bx = list(map(int,input().split()))

ax_ = (sorted(ax))
bx_ = (sorted(bx))
rx = [a > b for a,b in zip(ax_,bx_)]
if any(rx):
    print('No')
    exit()

ax = sorted([(i, a) for i, a in enumerate(ax)], key=lambda x:x[1])
#print(ax)
#exit()
ix = [i for i,a in enumerate(ax)]

p = c = 0
while True:
    c += 1
    p = ix[p]
    if p == 0:
        break
print(['No', 'Yes'][c != N])

