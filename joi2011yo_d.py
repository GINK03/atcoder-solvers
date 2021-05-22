
N=int(input())
A=list(map(int,input().split()))
 
dp=[[0]*21 for _ in range(101)]
dp[1][A[0]]=1
for i in range(0,N-1):
    for j in range(21):
        if j+A[i] <= 20:
            dp[i+1][j+A[i]]+=dp[i][j]
        if j-A[i] >= 0:
            dp[i+1][j-A[i]]+=dp[i][j]
print(dp[N-1][A[N-1]])

