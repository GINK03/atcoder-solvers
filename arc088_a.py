import itertools
X,Y=map(int,input().split())

x = X

cnt = 0
while True:
    cnt+=1
    x = 2*x
    if x > Y:
        break
print(cnt)

