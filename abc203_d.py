

N,K=map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N) ]

"""
F = []
for al in A:
    for a in al:
        F.append(a)
F.sort()

if K%2 == 0:
    print(F[K//2 * N])
else:
    print(F[K//2 * N + K//2])
"""


for i in range(N-K+1):
    A = [sorted(a) for a in A]
    s = [a[i:i+K] for a in A[i:i+K]]
    F = []
    for al in s:
        for a in al:
            F.append(a)
    F.sort()

    print(F)
    n = K

    print(F[n])


