n=int(input())
As = sorted(map(int,input().split()))

if As[0] == 0:
    print(0)
    exit()
b = 1
for a in reversed(As):
    b *= a
    if b > 10**18:
        print(-1)
        exit()
print(b)

