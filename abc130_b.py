n,x=map(int,input().split())
ls=list(map(int,input().split()))
c = 1
b = 0
for an in range(n):
    b+=ls[an]
    if b>x:
        break
    c+=1
print(c)
