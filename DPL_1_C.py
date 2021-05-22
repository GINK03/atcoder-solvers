
N,W=map(int,input().split())

VW=[]
for _ in range(N):
    v,w=map(int,input().split())
    VW.append( (v,w) )
dp = [0]*(W+10)
for v, w in VW:
    for j in range(len(dp)):
        if j >= w:
            dp[j] = max(dp[j-w]+v, dp[j])
#print(dp)
print(dp[W])
