
import sys; sys.setrecursionlimit(10**9)
N=int(input())
G=[[] for _ in range(N)]

AB = []
for _ in range(N-1):
    a,b=map(int,input().split())
    a-=1;b-=1
    AB.append( (a,b))
    G[a].append(b)
    G[b].append(a)

dp = [0]*N
def dfs(pos, prv):
    dp[pos] = 1
    for i in G[pos]:
        if i == prv:
            continue
        dfs(i, pos)
        dp[pos] += dp[i]
dfs(0,-1)
# print(dp) # 貢献度のリスト

ans = 0
for i in range(N-1):
    a,b=AB[i]
    r=min(dp[a], dp[b])
    ans += r*(N-r)
print(ans)
    


