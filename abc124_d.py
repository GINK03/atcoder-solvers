
import itertools
N,K = map(int, input().split())
S = input()
G = itertools.groupby(S)
L = []
for k,v in G:
    L.append(len(list(v)))

if S[0]=='0':
    L = [0]+L
AC = list(itertools.accumulate(L))+[0]
ans  = 0
lenL = len(L)
for i in range(0,lenL,2):
    l = i
    r = min(lenL-1,i+K*2)
    ans = max(ans,AC[r]-AC[l-1])
print(ans)
