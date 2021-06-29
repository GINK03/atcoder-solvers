

def prime_factorize(n: int) -> "List[int]":
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
    if a == []: # 入力が1のときの例外
        a.append(1)
    return a

A, B = map(int,input().split())

ap, bp = [set(prime_factorize(x)) for x in [A,B]]
ap.add(1)
bp.add(1)
print(len(ap & bp))

