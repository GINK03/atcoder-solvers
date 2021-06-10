
N,M=map(int,input().split())

dp=[0]*(1<<N); "ありえるパターンの大きさのリスト"
dp[0]=1

"もらうためのビットの対応を作る"
edge = [0]*N
for _ in range(M):
    x,y=map(int,input().split())
    edge[x-1] |= 1<<(y-1); "xはyより早くにゴールしたというbitパターンを記録"

for s in range(1<<N):
    for j in range(N):
        "sとjが共起したら"
        if s & (1<<j) > 0:
            "前に早くにゴールしたというパターンを持っていなければ"
            if s&edge[j] == 0:
                dp[s] += dp[s^(1<<j)]; "jがゴールしていない状態のbitパターンを貰う"

print(dp[-1])
