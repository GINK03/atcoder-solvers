
N,K=map(int,input().split())

def degit_sum(x):
    ret = 0
    while x > 0:
        ret += x%10
        x //= 10
    return ret

mod = 10**5

dp = [0]*mod
for i in range(mod):
    dp[i] = (i + degit_sum(i))%mod

ts = [-1]*mod
pos=N; cnt = 0
while ts[pos] == -1:
    ts[pos] = cnt
    pos = dp[pos]
    cnt += 1

cycle = cnt - ts[pos]
if K >= ts[pos]:
    K = (K-ts[pos])%cycle + ts[pos]

answer = -1
for i in range(mod):
    if ts[i] == K:
        answer = i

print(answer)

    
