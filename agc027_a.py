import itertools
N,x=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

for idx in range(N-1):
    if x - A[idx] < 0:
        print(idx)
        exit()
    x -= A[idx]

if x == A[-1]:
    print(N)
else:
    print(N-1)
