

N,K = map(int,input().split())
*A,=map(int,input().split())

base = K//N
mod = K%N

P = {}
for i, a in enumerate(sorted(A)):
    if i < mod:
        P[a] = base + 1
    else:
        P[a] = base

for a in A:
    print(P[a])
        


