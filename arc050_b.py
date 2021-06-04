
R,B=map(int,input().split())
X,Y=map(int,input().split())

def check(n):
    r = R-n
    b = B-n
    if r < 0 or b < 0:
        return False
    if r//(X-1) + b//(Y-1) >= n:
        return True
    else:
        return False


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(ng=10**20, ok=0))

