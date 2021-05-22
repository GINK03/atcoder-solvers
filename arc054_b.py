

P = float(input())

def f(x):
    return x + P*(2**(-x/1.5))


def check(n):
    d = (10**-9)
    return f(n+d) - f(n) < 0


ok = 0
ng = P
while True:
    mid = (ok + ng) / 2
    if check(mid):
        ok = mid
    else:
        ng = mid
    if ng - ok < 10**-8:
        break
print(f(ok))
