N=int(input())
A=list(map(lambda x:int(x)-1,input().split()))

X=[0]*N

for a in A:
    X[a]+=1

print(*X, sep='\n')


