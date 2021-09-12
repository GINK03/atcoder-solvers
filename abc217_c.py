
N = int(input())
*P, = map(int, input().split())

Q = [None]*N

for i, p in enumerate(P, 1):
    Q[p-1]=i

print(*Q)

