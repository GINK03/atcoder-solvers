A,B,K=map(int,input().split())
xs =[]
for i in range(1,101):
    if A%i == B%i == 0:
        xs.append(i)
print(xs[-K])

