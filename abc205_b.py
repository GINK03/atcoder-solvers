
N=int(input())
*A,=map(int,input().split())

A.sort()

if A == list(range(1, N+1)):
    print("Yes")
else:
    print("No")
