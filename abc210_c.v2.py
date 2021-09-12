import collections
N,K=map(int,input().split())
*C,=map(int,input().split())

tmp = collections.defaultdict(int)
for c in C[0:K]:
    tmp[c] += 1

ans = len(tmp)
buf = len(tmp)
for i in range(K, N):
    tmp[C[i]] += 1
    if tmp[C[i]] == 1:
        buf += 1
    
    tmp[C[i - K]] -= 1
    if tmp[C[i - K]] == 0:
        buf -= 1
    ans = max(ans, buf)
print(ans)

