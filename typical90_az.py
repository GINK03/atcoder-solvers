

N = int(input())
MOD = 10**9 + 7

acc = 1
for _ in range(N):
    *A,=map(int,input().split())
    acc *= sum(A)
    acc %= MOD
print(acc)

