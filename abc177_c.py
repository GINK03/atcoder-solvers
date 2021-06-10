
import itertools
N=int(input())
*A,=map(int,input().split())

B = [0] + list(itertools.accumulate(A))

MOD = 10**9 + 7
acc = 0
for i in range(N):
    acc += A[i] * B[i]
    acc %= MOD
print(acc%MOD)
