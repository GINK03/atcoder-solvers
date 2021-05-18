N=int(input())
H=list(map(int,input().split()))

C=[0]*(10**5)

C[0] = 0
C[1] = abs(H[1] - H[0])
#C[2] = min(abs(H[2] - H[0]) + C[0], abs(H[2] - H[1]) + C[1])


for i in range(2,N):
    for k in range(K):
    C[i] = min(abs(H[i] - H[i-2]) + C[i-2], abs(H[i] - H[i-1]) + C[i-1])

print(C[N-1])
