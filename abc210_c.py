
N,K=map(int,input().split())
*C,=map(int,input().split())

tmp = {}
for c in C[0:K]:
    if tmp.get(c) is None:
        tmp[c] = 0
    tmp[c] += 1


ans = len(tmp)
for i in range(K, N):
    if C[i] not in tmp:
        tmp[C[i]] = 0
    tmp[C[i]] += 1
    
    dc = C[i-K]
    tmp[dc] -= 1
    if tmp[dc] == 0:
        del tmp[dc]
    #print(i, tmp)
    ans = max(ans, len(tmp))
print(ans)

