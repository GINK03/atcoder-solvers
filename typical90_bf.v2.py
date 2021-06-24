
import collections

N,K=map(int,input().split())
def degit_sum(x):
    ret = 0
    while x > 0:
        ret += x%10
        x //= 10
    return ret
mod = 10**5
def fun(x):
    return (x + degit_sum(x))%mod
dp = collections.defaultdict(lambda :[0,0])
x = N; cnt = 0; dp[N] = [cnt, 1]
while True:
    x = fun(x)
    if dp[x][1] == 2:
        break
    cnt+=1
    dp[x][0] = cnt
    dp[x][1] += 1

head = [(val, cnt) for val, (cnt, freq) in dp.items() if freq == 1]
head.sort(key=lambda x:x[1])
*head,=map(lambda x:x[0], head)
cycle = [(val, cnt) for val, (cnt, freq) in dp.items() if freq == 2]
cycle.sort(key=lambda x:x[1])
*cycle,=map(lambda x:x[0], cycle)

if K < len(head):
    print(head[K])
else:
    K -= len(head)
    i = K%len(cycle)
    print(cycle[i])
