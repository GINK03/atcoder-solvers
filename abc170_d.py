import math
from collections import Counter


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)
    return arr


def primes(x):
    if x < 2:
        return []

    primes = [i for i in range(x)]
    primes[1] = 0  # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, x, prime):
            primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


ps = set(primes(10**6))

""" prime check """
input()
ai = list(map(int, input().split()))
aps = ([p for p in ai if p in ps])
# print("aps", aps)
cs = [c for c in ai if c not in ps]
cs.sort()
# print(cs)

def reduce_multiple(f):
    a = 1
    for f0 in f:
        a *= f0
    return a


def exists_in_aps(f):
    for f1 in f:
        if f1 in aps:
            return False
    else:
        return True


reduce_fs = set()
for c in cs:
    # print(c, sum([c%ap==0 for ap in aps]))
    if sum([c%ap==0 for ap in aps]) == 0:
        reduce_f = reduce_multiple(factorization(c))
        reduce_fs.add(reduce_f)

prime_num = 0
for p, n in Counter(aps).items():
    if n == 1:
        prime_num += 1
print(prime_num + len(reduce_fs))


"""
fs = [factorization(c) for c in cs]
fs = [f for f in fs if exists_in_aps(f)]
reduce_fs = set([reduce_multiple(f) for f in fs])
print(fs)

"""


