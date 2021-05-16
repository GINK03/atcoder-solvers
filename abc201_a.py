A=list(map(int,input().split()))
A.sort()
if A[2] - A[1] == A[1] - A[0]:
    print("Yes")
else:
    print("No")
