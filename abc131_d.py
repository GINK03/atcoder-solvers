n=int(input())

tmp=[]
for _ in range(n):
    tmp.append(list(map(int,input().split())))

tmp.sort(key=lambda x:x[1])

t = 0
for a,b in tmp:
    t+=a
    if b < t:
        print("No")
        exit()

print("Yes")
