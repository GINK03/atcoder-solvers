
N,S=map(int,input().split())

AB = []
for _ in range(N):
    a,b=map(int,input().split())
    AB.append( (a,b) )

dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = (1, "S")

for i in range(N):
    for j in range(S+1):
        if j - AB[i][0] >= 0:
            if dp[i][j - AB[i][0]] != 0:
                dp[i+1][j] = (j-AB[i][0], "A")
        if j - AB[i][1] >= 0:
            if dp[i][j - AB[i][1]] != 0:
                dp[i+1][j] = (j-AB[i][1], "B")

if dp[-1][S] == 0:
    print("Impossible")
    exit()


ans = []
icur = N
a = dp[icur][S]
scur = a[0]
ans.append(a[1])
while True:
    icur -= 1
    a = dp[icur][scur]
    if a[1] == "S":
        break
    ans.append(a[1])
    scur = a[0]

print("".join(ans[::-1]))
