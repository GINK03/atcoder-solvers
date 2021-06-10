
N=int(input())
*A,=map(int,input().split())
import math
tmp = A[0]
for a in A[1:]:
    tmp = math.gcd(tmp, a)
#if tmp >= 2:
#    print("not coprime")
#    exit()

import collections
AC = dict(collections.Counter(A))
flat = collections.defaultdict(int)
# コーナーケースハンドリング
if 1 in AC:
    flat[1]+=1

def sieve(n):
    dp = [1]*(n+1) # 初期値ですべてを素数と仮定
    dp[0] = 0

    for i in range(2, n+1):
        if dp[i]: # もし素数ならば
            if i in AC:
                flat[i] += AC[i] 
            j = 2 * i # iの倍数はすべて素数ではないはず
            while j <= n:
                dp[j] = 0
                if j in AC:
                    flat[i] += AC[j]
                j += i 

S=sieve(10**6 + 1000)
# print(flat)
*flat,=flat.values()
m = max(flat)
if m == 1:
    print("pairwise coprime")
elif m < N:
    print("setwise coprime")
else:
    print("not coprime")
