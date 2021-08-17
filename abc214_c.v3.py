
N = int(input())
*S, = map(int, input().split())
*T, = map(int, input().split())

L = [float("inf")]*N

for j in range(2):
    for i in range(N):
        L[i] = min(L[i-1] + S[i-1], T[i])
    
print(*L, sep="\n")

