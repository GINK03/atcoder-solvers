
# floor(N/m) = N%m 
# これは、 N = k*m + k -> N = k(m+1)
# となり約数の問題にすることができる
N=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
import math
ks = make_divisors(N)
ans = 0
for k in ks:
    # 式が成立するか
    if k == N:
        continue
    m = N//k-1
    if math.floor(N/m) == N%m:
        ans += m
print(ans)

