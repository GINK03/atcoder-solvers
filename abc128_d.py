N, K = map(int, input().split())
k = min(N,K)

vs = [int(v) for v in input().split()]

acts = []
for A in range(k):
    for B in range(k):
        if A+B>k:
            break
        acts.append((A,B))

ress = []
for A, B in acts:
    if A!=0:
        left = vs[:A]
    else:
        left = []
    if B!=0:
        right = vs[-B:]
    else:
        right =[]
    #print(A, B, left, right)
    join = left+right
    join = sorted(join)
    for l in range(K-A-B+1):
        res = sum(join[l:])
        ress.append(res)
print(max(ress))
