import collections

def main():
    MOD = 998244353
    N, M, K = map(int,input().split())
    G = [[] for n in range(N)]
    for m in range(M):
        u,v = map(int, input().split())
        u -= 1; v -= 1
        G[u].append(v)
        G[v].append(u)

    dp = [0]*N
    dp[0] = 1
    ndp = [0]*N
    for i in range(K):
        s = sum(dp)
        for n in range(N):
            ndp[n] = s - dp[n]
            for b in G[n]:
                ndp[n] -= dp[b]
        for n in range(N):
            dp[n] = ndp[n]%MOD
    print(dp[0])

if __name__ == "__main__":
    main()
