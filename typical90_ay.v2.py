import itertools
import collections
import bisect


def main():
    N,K,P=map(int,input().split())
    *A,=map(int,input().split())

    LA, RA = A[:N//2], A[N//2:]

    L=collections.defaultdict(list)
    for k in range(K+1):
        for la in itertools.combinations(LA, k):
            sum_ = 0 if la == [] else sum(la)
            L[k].append(sum_)

    R=collections.defaultdict(list)
    for k in range(K+1):
        for ra in itertools.combinations(RA, k):
            sum_ = 0 if ra == [] else sum(ra)
            R[k].append(sum_)

    for key in list(L.keys()):
        L[key].sort()
    for key in list(R.keys()):
        R[key].sort()

    ans = 0
    for rk, rlst in R.items():
        rem = K-rk
        llst = L[rem]
        for r in rlst:
            ans += bisect.bisect_left(llst, P-r + 1)
    print(ans)

if __name__ == "__main__":
    main()
"""
L=collections.defaultdict(list)
for i in range(1<<len(LA)):
    cnt = 0
    num = 0
    for j in range(len(LA)):
        if i&(1<<j) > 0:
            cnt += LA[j]
            num += 1
    L[num].append(cnt)
R=collections.defaultdict(list)
for i in range(1<<len(RA)):
    cnt = 0
    num = 0
    for j in range(len(RA)):
        if i&(1<<j) > 0:
            cnt += RA[j]
            num += 1
    R[num].append(cnt)
"""
