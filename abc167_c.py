from itertools import combinations


N,M,X=map(int,input().split())

mtable = [None]*N
cs = []
for n in range(N):
    aa = list(map(int,input().split()))
    c = aa.pop(0)
    cs.append(c)
    ms = aa
    mtable[n] = ms
    

# print(mtable)
idxes = list(range(N))

prices = []
for i in range(1, N+1):
    for c in combinations(idxes, i):
        sums = [0]*M
        for idx in c:
            for i, m in enumerate(mtable[idx]):
                sums[i] += m
        if all(map(lambda x:x >= X, sums)):
            price = 0
            for idx in c:
                price += cs[idx]

            prices.append(price)
if prices == []:
    print(-1)
else:
    print(min(prices))

