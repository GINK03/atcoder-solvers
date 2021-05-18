W=int(input())
N,K=map(int,input().split())

A=[]
for _ in range(N):
    # a: 幅
    # b: 重要度
    a,b=map(int,input().split())
    A.append( (a,b) )

MAX_W = 10000 + 10
dp = [[0 for _ in range(W + 1)] for _ in range(K + 1)]
for a, b in A:
  for i in reversed(range(K+1)):
    for j in range(W+1):
      if i>=1 and j>=a:
        dp[i][j]=max(dp[i][j], dp[i-1][j-a]+b)
print(dp[K][W])
