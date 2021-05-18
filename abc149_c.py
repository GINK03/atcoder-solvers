
X=int(input())

def sieve():
    n = 10**6
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i # iの倍数は自動的に素数ではないから
    for i in range(1, n+1):
        if is_prime[i-1]:
            if i >= X:
                print(i)
                exit()


sieve()



