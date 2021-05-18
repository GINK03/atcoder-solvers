import collections
MOD=10**9+7
N=int(input())

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

lst = []
for n in range(1,N+1):
    lst += prime_factorize(n)

ans = 1
for freq in collections.Counter(lst).values():
    ans = (ans*(freq+1))%MOD

print(ans%MOD)

