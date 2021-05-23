
N=int(input())
D=list(map(int,input().split()))

D.sort()
if len(D) in {0, 1} or len(D)%2 == 1:
    print(0)
    exit()
m = len(D)//2
if D[m-1] == D[m]:
    print(0)
    exit()
else:
    print(D[m] - D[m-1])
