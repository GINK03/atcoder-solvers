
N = int(input())
A = [int(input()) for n in range(N)]

ans = 0
for i in range(N):
    if A[i] == 0:
        continue
    if A[i]%2 == 0:
        ans += (A[i] - 2)//2
        A[i] = 2
    else:
        ans += A[i]//2
        A[i] = 1

for i in range(N):
    if i > 0 and A[i] > 0 and A[i-1] > 0:
        ans += 1
        A[i] -= 1
        A[i-1] -= 1
    if A[i] > 0 and A[i]%2 == 0:
        ans += 1
        A[i] = 0
    if N > i + 1 and A[i] > 0 and A[i+1] > 0:
        ans += 1
        A[i] -= 1
        A[i+1] -= 1

print(ans)

    
