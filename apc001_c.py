
N = int(input())
print(0, flush=True)
r = input()
if r == "Vacant":
    exit()
init = r

def query(mid):
    print(mid, flush=True)
    r = input()
    if r == "Vacant":
        exit()
    return int(r != init) # 相違していたら1

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        # ng条件: mid%2 == 0のときqueryが相違(vacantが含まれない)
        #       : mid%2 == 1のときqueryが一致
        if query(mid) == mid%2: 
            ng = mid
        else:
            ok = mid

    return ok
meguru_bisect(0, N)

