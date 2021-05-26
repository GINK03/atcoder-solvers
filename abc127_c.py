import collections
N,M=map(int,input().split())

L=collections.defaultdict(int)
R=collections.defaultdict(int)
for m in range(M):
    l,r=map(int,input().split())
    l-=1; r-=1
    L[l] += 1
    R[r+1] +=1

dp=[0]*N
st=0

for i in range(N):
    st += L[i]
    st -= R[i]
    dp[i] = st

print(dp.count(M))

