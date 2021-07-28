
N,X =map(int,input().split())
*A,=map(int,input().split())

for i in range(N):
    if i%2 == 1:
        A[i] -=1

if sum(A) <= X:
    print("Yes")
else:
    print("No")

