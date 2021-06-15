
N=int(input())
*A,=map(int,input().split())

for i in range(N):
    while A[i]%2 == 0:
        A[i]//=2
print(len(set(A)))
