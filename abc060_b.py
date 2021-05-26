
a,b,c=map(int,input().split())

for k in range(1, 1000):
    if (a*k)%b == c:
        print("YES")
        exit()
print("NO")

