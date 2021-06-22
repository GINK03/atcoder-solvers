import itertools
import collections

N,K,P=map(int,input().split())
*A,=map(int,input().split())

LA, RA = A[:N//2], A[N//2:]

L=collections.defaultdict(lambda :collections.defaultdict(int))
for k in range(K+1):
    for la in itertools.combinations(LA, k):
        sum_ = 0 if la == [] else sum(la) 
        L[k][sum_] += 1

R=collections.defaultdict(lambda :collections.defaultdict(int))
for k in range(K+1):
    for ra in itertools.combinations(RA, k):
        sum_ = 0 if ra == [] else sum(ra) 
        R[k][sum_] += 1


ans = 0
for rk, robj in R.items():
    rem = K-rk
    for rsum, rfreq in robj.items():
        for lsum, lfreq in L[rem].items():
            if rsum + lsum <= P:
                ans += rfreq * lfreq
print(ans)

