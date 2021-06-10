
N=int(input())
*A,=map(int,input().split())
A=[(a,i+1) for i,a in enumerate(A)]
A.sort()

for a, i in A[::-1]:
    print(i)
