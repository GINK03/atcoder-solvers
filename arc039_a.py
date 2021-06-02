
A,B=map(list,input().split())


r1 = list(map(str, range(1,10)))
r2 = list(map(str, range(0,10)))

def check(a, b):
    l = int("".join(a))
    r = int("".join(b))
    return l-r

ans = -float('inf')
for i in range(3):
    rot = r1 if i == 0 else r2
    a = A.copy()
    b = B.copy()
    for r in rot:
        a[i] = r
        ans = max(ans, check(a,b))
    a = A.copy()
    b = B.copy()
    for r in rot:
        b[i] = r
        ans = max(ans, check(a,b))
print(ans)

    


