
n, m = map(int,input().split())

bs=[None]*n

for i in range(m):
    a,b=map(int,input().split())
    a -= 1 
    if bs[a] is not None and bs[a] != b:
        print(-1)
        exit()

    bs[a] = b

if bs[0] == 0 and len(bs) >= 2:
    print(-1)
else:
    for i in range(len(bs)):
        if bs[i] is None:
            bs[i] = 0
    if bs[0] == 0 and len(bs) >= 2:
        bs[0] = 1
    print(''.join(map(str, bs)))
