import collections
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))


CI = collections.defaultdict(int)
for i,c in enumerate(C):
    CI[c] += 1

BI = collections.defaultdict(int)
for i,b in enumerate(B):
    BI[b] += CI[i+1] 

ans = 0
for a in A:
    if a not in BI:
        continue
    #for bi in BI[a]:
        #print(a, CI[bi])
    #    ans += len(CI[bi])
    ans += BI[a]
print(ans)

