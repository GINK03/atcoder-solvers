H, W = map(int,input().split())

t = 0
if H%2 == 0:
    t = H//2
else:
    t = H//2+1

if H == 1 or W == 1:
    print(1)
    exit(0)

if W%2 == 0:
    print(W//2*(H))
else:
    print(W//2*(H) + t)
