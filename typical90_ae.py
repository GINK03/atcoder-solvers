import collections


grundy = collections.defaultdict(int) # (k0, k1) -> int

for i in range(51):
    for j in range(1501):
        mex = [0]*1555
        if i >= 1:
            mex[grundy[(i-1,i+j)]] = 1
        if j >= 2:
            for k in range(1,j//2+1):
                mex[grundy[(i,j-k)]] = 1
        for k in range(1555):
            if mex[k] == 0:
                grundy[(i,j)] = k
                break


N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())

x=0
for i in range(N):
    x ^= grundy[(A[i],B[i])]

if x == 0:
    print("Second")
else:
    print("First")
