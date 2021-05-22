import collections
N, M = map(int, input().split())

A = set()
for _ in range(M):
    x, y = map(int, input().split())
    A.add((x - 1, y - 1))

ans = 0
P = 1 << N
for s in range(P):
    ok = 1
    for i in range(N):
        for j in range(i+1, N):
            if s&(1<<i) > 0 and s&(1 << j)>0:
                if (i, j) not in A:
                    ok = 0
    if ok: 
        ans = max(bin(s).count('1'), ans)
print(ans)
