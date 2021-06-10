
N,M=map(int,input().split())

dp=[0]*(1<<N)
dp[0]=1

edge = [0]*N
for _ in range(M):
    x,y=map(int,input().split())
    "xはyより早くにゴールしたという情報をyを起点に記録"
    edge[y-1] |= 1<<(x-1)

for s in range(1<<N):
    for j in range(N):
        "sとjが共起してなかったら"
        if s & (1<<j) == 0:
            "かつ、sと配る先が共起していなかったら"
            if s&edge[j] == 0:
                dp[s|(1<<j)] += dp[s]; "配る"

print(dp[-1])
