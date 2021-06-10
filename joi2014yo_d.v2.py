N=int(input())
S=input()
MOD=10007
# map = {'J':0, 'O': 1, 'I': 2}


dp = [[0]*(1<<3) for _ in range(N+1)]
dp[0][1] = 1; "この初期値は謎"

for day, s in enumerate(S):
    must_have = dict(J=0,O=1,I=2)[s]
    for i in range(1<<3):
        if i&(1<<must_have) > 0:
            for j in range(1<<3):
                if i&j > 0:
                    "貰うdp"
                    dp[day+1][i] += dp[day][j]
                    dp[day+1][i] %= MOD
print(sum(dp[-1])%MOD)

