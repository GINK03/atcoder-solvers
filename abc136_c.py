N = int(input())
Hs = list(map(int,input().split()))

Hs, HSs = Hs, sorted(Hs)
for h,s in zip(Hs, HSs):
    if h - s <= 1:
        ...
    else:
        print('No')
        exit()
print('Yes')
