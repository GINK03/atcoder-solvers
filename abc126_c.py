import math

N, K = map(int, input().split())

size = N

logK = math.log(K)
log2 = math.log(2)
log1_2 = math.log(1/2)
log1_N = math.log(1/N)

logPs = []
suffix = []
for n in [n+1 for n in range(N)]:
    # n*2**x >= K 
    if K <= n:
        suffix.append(1/N)
        continue
    x = math.ceil((logK-math.log(n))/log2)
    #print(n, x)
    logP = x*log1_2 + log1_N
    logPs.append(logP)

print(sum([math.exp(x) for x in logPs] + suffix))
