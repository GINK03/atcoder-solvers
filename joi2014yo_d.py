N=int(input())
S=input()
MOD = 10007
map = {'J':0, 'O': 1, 'I': 2}

P = 1<<3

dp = [0]*P
dp[1] = 1

for s in S:
    now = map[s]
    ndp = [0]*P
    for i in range(P):
        if i&(1<<now) == 0:
            continue
        for j in range(P):
            if i&j == 0:
                continue
            ndp[i] += dp[j]
            ndp[i] %= MOD
    dp = ndp
print(sum(dp)%MOD)

