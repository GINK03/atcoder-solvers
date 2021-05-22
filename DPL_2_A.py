import math

N,M = map(int,input().split())

STV = []
for m in range(M):
    s,t,v = list(map(int, input().split()))
    STV.append( (s,t,v) )

ALL = 1 << N
cost = []
for n in range(ALL):
    cost.append([math.inf] * N)
cost[0][0] = 0

def has_bit(n, i):
    return n & (1 << i) > 0

for n in range(ALL):
    for s, t, v in STV:
        # 宛先がすでに探索済みリストにいるとき or
        # 今いるところと宛先が同じ場合はキャンセル
        if has_bit(n, t) or s == t:
            continue
        # tビットを立てて更新する
        cost[n|(1<<t)][t] = min(cost[n|(1<<t)][t], cost[n][s] + v)

if cost[ALL-1][0] == math.inf:
    print(-1)
else:
    print(cost[ALL - 1][0])

