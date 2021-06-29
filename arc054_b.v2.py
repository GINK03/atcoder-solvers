import math

P = float(input())
    
def f(x):
    return x + P*(2**(-x/1.5))

def is_ok(x):
    # x + P*(2**(-x/1.5)) を微分すると
    # 1 + P * 2**(-x/1.5) * log 2 * (-1/1.5)
    if 1 + P * 2**(-x/1.5) * math.log(2) * (-1/1.5) > 0:
        return True
    return False

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 0.000000001):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(f(ok))
meguru_bisect(0, 10**20)
