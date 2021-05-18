import collections
import itertools
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N=int(input())

primes = prime_factorize(N)
primes = collections.Counter(primes)

acc = 0
for prime, freq in primes.items():
    for i in itertools.count(1):
        freq -= i
        if freq >= 0:
            acc += 1
        else:
            break
print(acc)

