N,K = map(int,input().split())
section = []
dp = [0]*(N+1)
S = [0]*(N+1)
MOD = 998244353
for _ in range(K):
    L,R = map(int,input().split())
    section.append((L,R))
 
section.sort()
dp[1] = 1
S[1] = 1
for i in range(2, N+1):
    for j in range(K):
        li = i - section[j][1]
        ri = i - section[j][0]
        
        if ri <= 0:
            continue
        li = max(li,1)
        dp[i] += (S[ri] - S[li-1]) % MOD
    
    S[i] = (dp[i] + S[i-1]) % MOD
 
print(dp[N] % MOD)
