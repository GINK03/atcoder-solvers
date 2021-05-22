
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i # iの倍数は自動的に素数ではないから
    table = [ i for i in range(1, n+1) if is_prime[i-1]] # 素数の列挙を得る
    return table


primes = sieve(10**5 + 10000)
set_primes = set(primes)
acc = [0]
for p in primes:
    if (p+1)//2 in set_primes:
        acc.append(acc[-1]+1)
    else:
        acc.append(acc[-1])
PI = {p:idx for idx, p in enumerate(primes)}
acc.pop(0)

acc2 = [0]
for i in range(1, 10**5):
    if i in set_primes:
        acc2.append(acc[PI[i]])
    else:
        acc2.append(acc2[-1])

Q=int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    print(acc2[r]-acc2[l-1])
