
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

# 2017に似た数を抽出
ps = set(primes)
p2017 = set()
for p in primes:
    if p in ps and (p+1)//2 in ps:
        p2017.add(p)

dp = [0] * (10**5 + 10)

for i in range(0, len(dp)):
    if i in p2017:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

Q = int(input())
for q in range(Q):
    l,r = map(int,input().split())
    print(dp[r]-dp[l-1])

# print(dp[:100])

