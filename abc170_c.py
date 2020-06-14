X,N=map(int,input().split())
if N==0:
    input()
    print(X)
    exit(0)
xn=list(map(int,input().split()))

a=[(abs(x-X),x) for x in xn]

for d in range(0, 100):
    a1=d+X 
    a2=-d+X
    if a2 not in xn:
        print(a2)
        exit(0)
    elif a1 not in xn:
        print(a1)
        exit(0)

