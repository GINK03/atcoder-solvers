
k=int(input())
a,b=map(int,input().split())

for x in range(a,b+1):
    if x%k == 0:
        print("OK")
        exit()
print("NG")
