x,y=map(int,input().split())

for i in range(0,x+1):
    k = x - i
    if i*2 + k*4 == y:
        print("Yes")
        exit()
print("No")
