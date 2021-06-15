
N,K=map(int,input().split())
*X,=map(int,input().split())
P=[0] + list(filter(lambda x:x>=0, X))
N=[0] + [-x for x in filter(lambda x:x<0, X)][::-1]


ans = float("inf")
for k in range(K):
    if k >= len(P):
        break
    pk = P[k]
    if K-k >= len(N):
        continue
    nk = N[K-k]
    ans = min(ans, pk + nk + min(pk, nk))
for k in range(K):
    if k >= len(N):
        break
    nk = N[k]
    if K-k >= len(P):
        continue
    pk = P[K-k]
    ans = min(ans, pk + nk + min(pk, nk))
print(ans)
