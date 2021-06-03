
N,L=map(int,input().split())
K=int(input())
*A,=map(int,input().split())

def check(n):
    pre = 0 
    split = 0
    for a in A:
        if a - pre >= n and L - a >= n:
            split += 1
            pre = a
    return split >= K

ok = 0
ng = 10 ** 20
while True:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
    if ng - ok == 1:
        break
print(ok)
